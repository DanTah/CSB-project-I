# Pylint-raportti

Pylint antaa seuraavan raportin sovelluksesta:
```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:33:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:54:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:65:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:71:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:124:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:153:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:174:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:183:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:183:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:214:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:229:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:229:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:269:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:312:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:312:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:334:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:346:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:350:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:371:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:371:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:389:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:395:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:399:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module recipes
recipes.py:1:0: C0114: Missing module docstring (missing-module-docstring)
recipes.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:16:0: R0913: Too many arguments (6/5) (too-many-arguments)
recipes.py:16:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
recipes.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:74:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:89:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:102:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:106:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:106:0: R0913: Too many arguments (6/5) (too-many-arguments)
recipes.py:106:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
recipes.py:116:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:128:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:133:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:140:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:162:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:176:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:176:0: R0913: Too many arguments (6/5) (too-many-arguments)
recipes.py:176:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
recipes.py:192:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:198:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module seed
seed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
seed.py:11:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:12:0: C0103: Constant name "recipe_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:13:0: C0103: Constant name "review_count" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:1:0: R0801: Similar lines in 2 files
==recipes:[140:153]
==users:[11:24]
    sql = """SELECT recipes.id,
                    recipes.title,
                    recipes.recipe_time,
                    users.id user_id,
                    users.username,
                    CASE WHEN AVG(reviews.rating) = CAST(
                            AVG(reviews.rating) AS INTEGER)
                         THEN CAST(AVG(reviews.rating) AS INTEGER)
                         ELSE ROUND(AVG(reviews.rating), 2)
                    END AS avg_rating
             FROM users, recipes
             LEFT JOIN reviews
             ON recipes.id = reviews.recipe_id (duplicate-code)
users.py:1:0: R0801: Similar lines in 2 files
==recipes:[16:23]
==seed:[25:31]
    sql = """INSERT INTO recipes (title, recipe_time, ingredients,
                                  instructions, user_id, image)
             VALUES (?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [title, recipe_time, ingredients,
                     instructions, user_id, image])

def add_classes(recipe_id, classes): (duplicate-code)

------------------------------------------------------------------
Your code has been rated at 8.48/10 (previous run: 8.48/10, +0.00)
```
Käydään seuraavaksi raportin sisältö läpi perustellaan, ja perustellaan miksi asioita ei ole korjattu sovelluksessa.

## Missing docstring -ilmoitukset
Sovelluksen kehityksen aikana olen päättänyt olla käyttämättä moduuleissa ja funktioissa dockstring -kommentteja.
```
C0114: Missing module docstring (missing-module-docstring)
C0116: Missing function or method docstring (missing-function-docstring)
```
Nämä Pylintin antamat ilmoitukset johtuvat juuri tästä valinnasta.

## inconsistent-return-statements -ilmoitukset
Raportissa on myös ilmoituksia funktion paluuarvoon liittyen.
```
R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```
Raportin ilmoitukset liittyvät funktioiden tapaan käsitellä `GET` ja `POST` -metodeja. Ilmoitus koskee esimerkiksi seuraavaa funktiota:
```
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
        return redirect("/recipe/"+str(recipe_id))
```
Kyseinen funktio palauttaa arvon vain, jos `request.method` on `GET` tai `POST`. Koska funktiossa ei käsitellä
muita tilanteita, antaa Pylint tästä huomautuksen. Tämän sovelluksen tapauksessa ei kuitenkaan ole mahdollista,
että `request.method` saisi muita arvoja, koska dekoraattorissa `@app.route` jo vaaditaan, että metodin on oltava
`GET` tai `POST`. Näin ollen tämäkin ilmoitus sivuutetaan.

## invalid-name -ilmoitukset
Raportissa on myös vakion nimeen liittyviä ilmoituksia:
```
C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
```
Ilmoituksessa siis huomautetaan, että päätasolla määritetty vakioarvoinen muuttuja tulisi nimetä isoilla
kirjaimilla. Sovelluksen kehittäjän mielestä sovelluksessa näyttää kuitenkin paremmalle, että muuttujia merkitään
pienillä kirjaimilla.

## dangerous-default-value -ilmoitukset
Raportissa on myös oletusarvoon liittyviä ilmoituksia:
```
Dangerous default value [] as argument (dangerous-default-value)
```
Ilmoitus koskee esimekriksi seuraavaa funktiota:
```
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
```
Tyhjä lista voi olla vaarallinen oletusarvo funktion argumentille, jos jossain kutsussa listan sisältö muuttuisi.
Tämä muutos säilyisi myös seuraaviin kutsuihin asti. Koska koodi ei kuitenkaan muuta tätä listaoliota, 
sivuutetaan tämäkin ilmoitus.

## too-many-arguments - ja too-many-positional-arguments -ilmoitukset
Raportissa on myös argumenttien määrään liittyviä ilmoituksia:
```
R0913: Too many arguments (6/5) (too-many-arguments)
R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
```
Pylint ilmoittaa tästä, koska suuri määrä argumentteja funktiossa voi tehdä
tulkinnasta ja ylläpitämisestä tapreettoman mutkikasta ja sekavaa. Koska jokaisessa ilmoitusta koskevassa funktiossa
on kuitenkin kuusi argumenttia pylintin suositteleman viiden sijaan, kehittäjän mielestä tämä ei ole vielä tarpeellista.

## duplicate-code -ilmoitukset
Pylint ilmoittaa myös jos peräkkäiset rivit koodia toistuvat. Koodia, mikä toistuu useassa osassa sovellusta voi olla
työlästä ylläpitää. Sovelluksen kehittäjän mielestä toistuvaa koodia ei ole kuitenkaan tarpeettoman paljon ja
tiedoston `seed.py` tarkoitus on lähinnä testata sivun latausnopeutta, joten ilmoitukset on jätetty huomiotta.
