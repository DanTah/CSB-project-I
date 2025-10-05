import db

def get_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)
    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)
    return classes

def add_recipe(title, recipe_time, ingredients, instructions, user_id, classes):
    sql = """INSERT INTO recipes (title, recipe_time, ingredients, instructions, user_id) VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, recipe_time, ingredients, instructions, user_id])

    recipe_id = db.last_insert_id()
    sql = """INSERT INTO classes_in_recipe (recipe_id, title, value) VALUES (?, ?, ?)"""
    for title, value in classes:
        db.execute(sql, [recipe_id, title, value])

def get_classes_in_recipe(recipe_id):
    sql = """SELECT title, value
    FROM classes_in_recipe
    WHERE recipe_id = ?"""
    result = db.query(sql,[recipe_id])
    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)
    return classes

def get_recipes():
    sql = "SELECT id,title FROM recipes ORDER BY id DESC"
    return db.query(sql)

def get_recipe(recipe_id):
    sql = """SELECT u.id user_id,
                    u.username,
                    r.id,
                    r.title,
                    r.recipe_time,
                    r.ingredients,
                    r.instructions
             FROM users u, recipes r where r.user_id = u.id and r.id = ?"""
    if db.query(sql,[recipe_id]):
        return db.query(sql,[recipe_id])[0]
    return None

def update_recipe(recipe_id, title, recipe_time, ingredients, instructions, classes):
    sql = """ UPDATE recipes SET title = ?,
                                 recipe_time = ?,
                                 ingredients = ?,
                                 instructions = ?
                             WHERE id = ?"""
    sql = "DELETE FROM classes_in_recipe WHERE item_id = ?"
    db.execute(sql,[recipe_id])
    db.execute(sql, [title,recipe_time,ingredients,instructions,recipe_id])
    sql = """INSERT INTO classes_in_recipe (recipe_id, title, value) VALUES (?, ?, ?)"""
    for title, value in classes:
        db.execute(sql, [recipe_id, title, value])



def remove_recipe(recipe_id):
    sql = """DELETE FROM classes_in_recipe WHERE recipe_id = ?"""
    db.execute(sql,[recipe_id])
    sql = """DELETE FROM recipes WHERE id = ?"""
    db.execute(sql,[recipe_id])

def find_recipes(query):
    sql = """SELECT id, title
             FROM recipes
             WHERE LOWER(title) like LOWER(('%') || ? || ('%'))
             OR LOWER(ingredients) like LOWER(('%') || ? || ('%'))
             ORDER BY id DESC"""
    return db.query(sql,[query,query])
