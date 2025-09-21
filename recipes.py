import db

def add_recipe(title, recipe_time, ingredients, instructions, user_id):
    sql = """INSERT INTO recipes (title, recipe_time, ingredients, instructions, user_id) VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, recipe_time, ingredients, instructions, user_id])
