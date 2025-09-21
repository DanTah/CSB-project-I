import db

def add_recipe(title, recipe_time, ingredients, instructions, user_id):
    sql = """INSERT INTO recipes (title, recipe_time, ingredients, instructions, user_id) VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, recipe_time, ingredients, instructions, user_id])

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
    return db.query(sql,[recipe_id])[0]

def update_recipe(recipe_id, title, recipe_time, ingredients, instructions):
    sql = """ UPDATE recipes SET title = ?,
                                 recipe_time = ?,
                                 ingredients = ?,
                                 instructions = ?
                             WHERE id = ?"""
    db.execute(sql, [title,recipe_time,ingredients,instructions,recipe_id])
