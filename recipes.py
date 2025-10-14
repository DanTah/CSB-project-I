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

def add_recipe(title, recipe_time, ingredients, instructions, user_id, classes, image):
    sql = """INSERT INTO recipes (title, recipe_time, ingredients, instructions, user_id, image) VALUES (?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [title, recipe_time, ingredients, instructions, user_id, image])

    recipe_id = db.last_insert_id()
    sql = """INSERT INTO classes_in_recipe (recipe_id, title, value) VALUES (?, ?, ?)"""
    for title, value in classes:
        db.execute(sql, [recipe_id, title, value])

def get_last_recipe_id():
    sql ="""SELECT MAX(id) FROM recipes"""
    return db.query(sql)[0]

def get_image(recipe_id):
    sql = "SELECT image FROM recipes WHERE id=?"
    result = db.query(sql,[recipe_id])
    return result[0][0] if result else None

def add_review(recipe_id, user_id, rating, comment, date):
    sql = """INSERT INTO reviews (recipe_id, user_id, rating, comment, date) VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [recipe_id, user_id, rating, comment, date])

def get_reviews(recipe_id):
    sql = """SELECT users.id user_id, users.username, reviews.id review_id, reviews.rating, reviews.comment, reviews.date
             FROM users, reviews
             WHERE reviews.recipe_id = ? AND reviews.user_id = users.id
             ORDER BY reviews.id DESC"""
    return db.query(sql, [recipe_id])

def get_review(recipe_id,user_id):
    sql = """SELECT users.id user_id, users.username, reviews.id review_id, reviews.rating, reviews.comment, reviews.date
             FROM users, reviews
             WHERE reviews.recipe_id = ? AND reviews.user_id = users.id
             AND reviews.user_id = ?"""
    if db.query(sql, [recipe_id,user_id]):
        return db.query(sql, [recipe_id,user_id])[0]
    return None

def get_review_by_id(review_id):
    sql = """SELECT users.id user_id, users.username, reviews.id review_id, reviews.rating, reviews.comment, reviews.date
             FROM users, reviews
             WHERE reviews.id = ? AND reviews.user_id = users.id"""
    if db.query(sql, [review_id]):
        return db.query(sql, [review_id])[0]
    return None

def remove_review(review_id):
    sql = """DELETE FROM reviews WHERE id = ?"""
    db.execute(sql,[review_id])

def update_review(review_id, recipe_id, user_id, rating, comment, date):
    sql = """ UPDATE reviews
              SET recipe_id = ?,user_id = ?,rating = ?,comment = ?,date = ?
              WHERE id = ?"""
    db.execute(sql,[recipe_id,user_id,rating,comment,date,review_id])

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
                    r.instructions,
                    r.image IS NOT NULL has_image
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
    db.execute(sql,[title,recipe_time,ingredients,instructions,recipe_id])
    sql = "DELETE FROM classes_in_recipe WHERE recipe_id = ?"
    db.execute(sql,[recipe_id])
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
