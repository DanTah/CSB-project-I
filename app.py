import sqlite3
from datetime import datetime
from flask import Flask
from flask import abort, redirect, render_template, request, \
    session, flash, make_response
import db
import config
import recipes
import users
import markupsafe
import secrets


app = Flask(__name__)
app.secret_key = config.secret_key

def check_csrf():
    if "csrf_token" not in request.form:
        abort(403)
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br />")
    return markupsafe.Markup(content)

@app.route("/")
def index():
    all_recipes = recipes.get_recipes()
    classes = {}
    for recipe in all_recipes:
        classes[recipe["id"]] = recipes.get_recipe_classes(recipe["id"])
    return render_template("index.html", recipes = all_recipes,
                            classes = classes)

@app.route("/find_recipe")
def find_recipe():
    query = request.args.get("query")
    results = recipes.find_recipes(query) if query else []
    classes = {}
    for recipe in results:
        classes[recipe["id"]] = recipes.get_recipe_classes(recipe["id"])
    return render_template("find_recipe.html", query = query,
                           results = results, classes = classes)

@app.route("/new_recipe")
def new_recipe():
    require_login()
    classes = recipes.get_classes()
    return render_template("new_recipe.html", classes = classes)

@app.route("/create_recipe", methods = ["POST"])
def create_recipe():
    require_login()
    check_csrf()

    title = request.form["title"]
    if not title or len(title) > 65:
        abort(403)
    recipe_time = request.form["recipe_time"]
    if not (recipe_time and is_int(recipe_time) and \
            1 <= int(recipe_time) <= 999):
        abort(403)
    ingredients = request.form["ingredients"]
    if not ingredients or len(ingredients) > 1000:
        abort(403)
    instructions = request.form["instructions"]
    if not instructions or len(instructions) > 3000:
        abort(403)
    user_id = session["user_id"]

    all_classes = recipes.get_classes()
    classes = []
    entries = request.form.getlist("classes")
    if entries:
        for entry in request.form.getlist("classes"):
            if entry == "":
                continue
            class_title, class_value = entry.split(":")
            if class_title not in all_classes or \
               class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    file = request.files["image"]
    image = file.read()
    if image:
        if not file.filename.endswith((".png", ".jpg", ".jpeg")):
            flash("VIRHE: väärä tiedostomuoto")
            return redirect("/new_recipe")
        if len(image) > 100 * 1024:
            flash("VIRHE: liian suuri kuva")
            return redirect("/new_recipe")
    else:
        image = None

    recipes.add_recipe(title, recipe_time, ingredients,
                       instructions, user_id, image)
    recipe_id = db.last_insert_id()
    recipes.add_classes(recipe_id, classes)
    flash("Resepti on lisätty onnistuneesti")
    return redirect("/recipe/"+str(recipe_id))

@app.route("/recipe/<int:recipe_id>")
def show_recipe(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    classes = recipes.get_recipe_classes(recipe_id)
    reviews = recipes.get_reviews(recipe_id)
    recipe_rating = recipes.get_avg_rating(recipe_id)

    my_review = None
    if "user_id" in session:
        my_review = recipes.get_review(recipe_id, session["user_id"])
    return render_template("show_recipe.html", recipe = recipe,
                           reviews = reviews, recipe_rating = recipe_rating,
                           my_review = my_review, classes = classes)

@app.route("/create_review", methods = ["POST"])
def create_review():
    require_login()
    check_csrf()

    rating = request.form["rating"]
    if not (is_int(rating) and 1 <= int(rating) <= 5):
        abort(403)
    comment = request.form["comment"]
    if not comment or len(comment) > 2000:
        abort(403)
    date = datetime.today().strftime('%d.%m.%Y')
    recipe_id = request.form["recipe_id"]
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    user_id = session["user_id"]

    recipes.add_review(recipe_id, user_id, rating, comment, date)
    return redirect("/recipe/"+str(recipe_id))

@app.route("/image/<int:recipe_id>")
def show_image(recipe_id):
    image = recipes.get_image(recipe_id)
    if not image:
        abort(404)
    response = make_response(bytes(image))
    response.headers.set("Content-Type", "image")
    return response

@app.route("/new_image/<int:recipe_id>", methods = ["GET", "POST"])
def new_image(recipe_id):
    require_login()

    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("new_image.html", recipe = recipe)

    if request.method == "POST":
        check_csrf()

        file = request.files["image"]
        image = file.read()
        if image:
            if not file.filename.endswith((".png", ".jpg", ".jpeg")):
                flash("VIRHE: väärä tiedostomuoto")
                return redirect("/new_image/"+str(recipe_id))
            if len(image) > 100 * 1024:
                flash("VIRHE: liian suuri kuva")
                return redirect("/new_image/"+str(recipe_id))
        else:
            image = None
        recipes.update_image(recipe_id, image)
        flash("Kuva on vaihdettu onnistuneesti")
        return redirect("/recipe/"+str(recipe_id))

@app.route("/edit_recipe/<int:recipe_id>")
def edit_recipe(recipe_id):
    require_login()

    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)
    classes = recipes.get_recipe_classes(recipe_id)
    all_classes = recipes.get_classes()
    return render_template("edit_recipe.html", recipe = recipe,
                           classes = classes, all_classes = all_classes)

@app.route("/recipe/<int:recipe_id>/edit_review/<int:review_id>",
           methods = ["GET", "POST"])
def edit_review(recipe_id, review_id):
    require_login()

    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    my_review = recipes.get_review_by_id(review_id)
    if not my_review:
        abort(404)
    if my_review["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("edit_review.html", my_review = my_review,
                               recipe = recipe)

    if request.method == "POST":
        check_csrf()

        if "remove" in request.form:
            recipes.remove_review(review_id)
            return redirect("/recipe/"+str(recipe_id))
        if "back" in request.form:
            return redirect("/recipe/"+str(recipe_id))
        if "update" in request.form:
            user_id = session["user_id"]
            rating = request.form["rating"]
            if not (is_int(rating) and 1 <= int(rating) <= 5):
                abort(403)
            comment = request.form["comment"]
            if not comment or len(comment) > 2000:
                abort(403)
            date = datetime.today().strftime('%d.%m.%Y')

            recipes.update_review(review_id, recipe_id, user_id,
                                  rating, comment, date)
            flash("Arvio on muokattu onnistuneesti")
            return redirect("/recipe/"+str(recipe_id))

@app.route("/update_recipe", methods = ["POST"])
def update_recipe():
    require_login()
    check_csrf()

    recipe_id = request.form["recipe_id"]
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)
    title = request.form["title"]
    if not title or len(title) > 65:
        abort(403)
    recipe_time = request.form["recipe_time"]
    if not (recipe_time and is_int(recipe_time) and \
            1 <= int(recipe_time) <= 999):
        abort(403)
    ingredients = request.form["ingredients"]
    if not ingredients or len(ingredients) > 1000:
        abort(403)
    instructions = request.form["instructions"]
    if not instructions or len(instructions) > 3000:
        abort(403)

    all_classes = recipes.get_classes()
    classes = []
    entries = request.form.getlist("classes")
    if entries:
        for entry in request.form.getlist("classes"):
            if entry == "":
                continue
            class_title, class_value = entry.split(":")
            if class_title not in all_classes or \
               class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    recipes.update_recipe(recipe_id, title, recipe_time,
                          ingredients, instructions, classes)
    flash("Resepti on päivitetty onnistuneesti")
    return redirect("/recipe/"+str(recipe_id))

@app.route("/remove_recipe/<int:recipe_id>", methods = ["GET", "POST"])
def remove_recipe(recipe_id):
    require_login()

    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_recipe.html", recipe = recipe)

    if request.method == "POST":
        check_csrf()

        if "remove" in request.form:
            recipes.remove_recipe(recipe_id)
            flash("Resepti on poistettu onnistuneesti")
            return redirect("/")
        else:
            return redirect("/recipe/"+str(recipe_id))

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    user_recipes = users.get_recipes(user_id)
    if not user:
        abort(404)
    classes = {}
    for recipe in user_recipes:
        classes[recipe["id"]] = recipes.get_recipe_classes(recipe["id"])
    return render_template("show_user.html", user = user,
                           recipes = user_recipes, classes = classes)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods = ["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if not (password1 and password2):
        flash("VIRHE: salasanaa ei annettu")
        return redirect("/register")
    if password1 != password2:
        flash("VIRHE: salasanat eivät ole samat")
        return redirect("/register")

    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        flash("VIRHE: tunnus on jo varattu")
        return redirect("/register")

    flash("Tunnusten luonti onnistui")
    return redirect("/login")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            flash("VIRHE: väärä tunnus tai salasana")
            return redirect("/login")

@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    flash("Uloskirjautuminen onnistui")
    return redirect("/")

def require_login():
    if "user_id" not in session:
        abort(403)

def is_int(value):
  if value is None:
      return False
  try:
      int(value)
      return True
  except:
      return False
