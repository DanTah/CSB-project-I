import sqlite3
from datetime import datetime
from flask import Flask
from flask import abort, redirect, render_template, request, session
import db
import config
import recipes
import users
app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    all_recipes = recipes.get_recipes()
    return render_template("index.html", recipes = all_recipes)

@app.route("/find_recipe")
def find_recipe():
    query = request.args.get("query")
    results = recipes.find_recipes(query) if query else []
    return render_template("find_recipe.html", query=query, results = results)

@app.route("/new_recipe")
def new_recipe():
    require_login()
    classes = recipes.get_classes()
    return render_template("new_recipe.html", classes = classes)

@app.route("/create_review",methods = ["POST"])
def create_review():
    require_login()
    rating = request.form["rating"]
    if not (is_int(rating) and  1<=int(rating)<=5):
        abort(403)
    comment = request.form["comment"]
    if not comment or len(comment)>2000:
        abort(403)
    date = datetime.today().strftime('%d.%m.%Y')
    recipe_id = request.form["recipe_id"]
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    user_id = session["user_id"]
    recipes.add_review(recipe_id, user_id, rating, comment, date)
    return redirect("/recipe/"+str(recipe_id))

@app.route("/create_recipe",methods = ["POST"])
def create_recipe():
    require_login()
    title = request.form["title"]
    if not title or len(title)>65:
        abort(403)
    recipe_time = request.form["recipe_time"]
    if  not recipe_time or int(recipe_time)>999:
        abort(403)
    ingredients = request.form["ingredients"]
    if not ingredients or len(ingredients)>1000:
        abort(403)
    instructions = request.form["instructions"]
    if not instructions or len(instructions)>1000:
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
            if class_title not in all_classes or class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))
    recipes.add_recipe(title, recipe_time, ingredients, instructions, user_id, classes)
    return redirect("/")

@app.route("/recipe/<int:recipe_id>")
def show_recipe(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    classes = recipes.get_classes_in_recipe(recipe_id)
    reviews = recipes.get_reviews(recipe_id)
    return render_template("show_recipe.html", recipe = recipe, reviews = reviews, classes = classes)

@app.route("/edit_recipe/<int:recipe_id>")
def edit_recipe(recipe_id):
    require_login()
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] == session["user_id"]:
        classes = recipes.get_classes_in_recipe(recipe_id)
        all_classes = recipes.get_classes()
        return render_template("edit_recipe.html",recipe = recipe, classes = classes, all_classes = all_classes)
    abort(403)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    recipes = users.get_recipes(user_id)
    if not user:
        abort(404)
    return render_template("show_user.html", user = user, recipes = recipes)

@app.route("/update_recipe",methods = ["POST"])
def update_recipe():
    require_login()
    recipe_id = request.form["recipe_id"]
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)
    title = request.form["title"]
    if not title or len(title)>65:
        abort(403)
    recipe_time = request.form["recipe_time"]
    if  not recipe_time or int(recipe_time)>999:
        abort(403)
    ingredients = request.form["ingredients"]
    if not ingredients or len(ingredients)>1000:
        abort(403)
    instructions = request.form["instructions"]
    if not instructions or len(instructions)>1000:
        abort(403)
    all_classes = recipes.get_classes()
    classes = []
    entries = request.form.getlist("classes")
    if entries:
        for entry in request.form.getlist("classes"):
            if entry == "":
                continue
            class_title, class_value= entry.split(":")
            if class_title not in all_classes or class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))
    recipes.update_recipe(recipe_id, title, recipe_time, ingredients, instructions, classes)
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
        return render_template("remove_recipe.html",recipe = recipe)
    if request.method == "POST":
        if "remove" in request.form:
            recipes.remove_recipe(recipe_id)
            return redirect("/")
        else:
            return redirect("/recipe/"+str(recipe_id))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    try:
        users.create_user(username,password1)
    except sqlite3.IntegrityError:
        return "Virhe: tunnus on jo varattu"
    return "Tunnus luotu"

@app.route("/login", methods=["GET","POST"])
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
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
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
