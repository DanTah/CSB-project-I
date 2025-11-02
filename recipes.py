import db

def get_classes():
    sql = """SELECT title, value
             FROM classes
             ORDER BY id"""
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)
    return classes

def add_recipe(title, recipe_time, ingredients, instructions, user_id, image):
    sql = """INSERT INTO recipes (title, recipe_time, ingredients,
                                  instructions, user_id, image)
             VALUES (?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [title, recipe_time, ingredients,
                     instructions, user_id, image])

def add_classes(recipe_id, classes):
    sql = """INSERT INTO classes_in_recipe (recipe_id, title, value)
             VALUES (?, ?, ?)"""
    for title, value in classes:
        db.execute(sql, [recipe_id, title, value])

def get_image(recipe_id):
    sql = """SELECT image
             FROM recipes
             WHERE id=?"""
    result = db.query(sql, [recipe_id])
    return result[0][0] if result else None

def update_image(recipe_id, image):
    sql = """UPDATE recipes
             SET image = ?
             WHERE id = ?"""
    db.execute(sql, [image, recipe_id])

def add_review(recipe_id, user_id, rating, comment, date):
    sql = """INSERT INTO reviews (recipe_id, user_id, rating, comment, date)
             VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [recipe_id, user_id, rating, comment, date])

def get_reviews(recipe_id, page, page_size):
    sql = """SELECT users.id user_id,
                    users.username,
                    reviews.id review_id,
                    reviews.rating,
                    reviews.comment,
                    reviews.date
             FROM users, reviews
             WHERE reviews.recipe_id = ? AND reviews.user_id = users.id
             ORDER BY reviews.id DESC
             LIMIT ? OFFSET ?"""
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [recipe_id, limit, offset])

def get_avg_rating(recipe_id):
    sql = """SELECT avg(rating)
             FROM (SELECT rating
                   FROM reviews
                   WHERE recipe_id = ?)"""
    result = db.query(sql, [recipe_id])[0][0]
    if result:
        if result.is_integer():
            return int(result)
        return round(result, 2)
    return None

def get_review(recipe_id, user_id):
    sql = """SELECT users.id user_id,
                    users.username,
                    reviews.id review_id,
                    reviews.rating,
                    reviews.comment,
                    reviews.date
             FROM users, reviews
             WHERE reviews.recipe_id = ?
             AND reviews.user_id = users.id
             AND reviews.user_id = ?"""
    if db.query(sql, [recipe_id, user_id]):
        return db.query(sql, [recipe_id, user_id])[0]
    return None

def get_review_by_id(review_id):
    sql = """SELECT users.id user_id,
                    users.username,
                    reviews.id review_id,
                    reviews.rating,
                    reviews.comment,
                    reviews.date
             FROM users, reviews
             WHERE reviews.id = ? AND reviews.user_id = users.id"""
    if db.query(sql, [review_id]):
        return db.query(sql, [review_id])[0]
    return None

def remove_review(review_id):
    sql = "DELETE FROM reviews WHERE id = ?"
    db.execute(sql, [review_id])

def update_review(review_id, recipe_id, user_id, rating, comment, date):
#    sql = """ UPDATE reviews
#              SET recipe_id = ?,
#                  user_id = ?,
#                  rating = ?,
#                  date = ?,
#                  comment = ? WHERE id = ?"""
#    db.execute(sql, [recipe_id, user_id, rating, date, comment, review_id])
    sql = f""" UPDATE reviews
               SET recipe_id = {recipe_id},
                   user_id = {user_id},
                   rating = {rating},
                   date = '{date}',
                   comment = '{comment}' WHERE id = {review_id}"""
    db.execute(sql)

def get_recipe_classes(recipe_id):
    sql = """SELECT title, value
             FROM classes_in_recipe
             WHERE recipe_id = ?"""
    result = db.query(sql, [recipe_id])
    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)
    return classes

def recipe_count():
    sql = "SELECT count(id) FROM recipes"
    result = db.query(sql)[0][0]
    return result if result > 0 else 0

def review_count(recipe_id):
    sql = """SELECT count(id)
             FROM reviews
             WHERE recipe_id = ?"""
    result = db.query(sql, [recipe_id])[0][0]
    return result if result > 0 else 0

def get_recipes(page,page_size):
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
             ON recipes.id = reviews.recipe_id
             WHERE recipes.user_id = users.id
             GROUP BY recipes.id
             ORDER BY recipes.id DESC
             LIMIT ? OFFSET ?"""
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [limit, offset])

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
    if db.query(sql, [recipe_id]):
        return db.query(sql, [recipe_id])[0]
    return None

def update_recipe(recipe_id, title, recipe_time,
                  ingredients, instructions, classes):
    sql = """ UPDATE recipes
              SET title = ?,
                  recipe_time = ?,
                  ingredients = ?,
                  instructions = ?
              WHERE id = ?"""
    db.execute(sql, [title, recipe_time, ingredients, instructions, recipe_id])
    sql = "DELETE FROM classes_in_recipe WHERE recipe_id = ?"
    db.execute(sql, [recipe_id])
    sql = """INSERT INTO classes_in_recipe (recipe_id, title, value)
             VALUES (?, ?, ?)"""
    for class_title, class_value in classes:
        db.execute(sql, [recipe_id, class_title, class_value])

def remove_recipe(recipe_id):
    sql = "DELETE FROM classes_in_recipe WHERE recipe_id = ?"
    db.execute(sql, [recipe_id])
    sql = "DELETE FROM reviews WHERE recipe_id = ?"
    db.execute(sql, [recipe_id])
    sql = "DELETE FROM recipes WHERE id = ?"
    db.execute(sql, [recipe_id])

def find_recipes(query, page_size):
    sql = """SELECT recipes.id,
                    recipes.recipe_time,
                    recipes.title,
                    users.id user_id,
                    users.username,
                    CASE WHEN AVG(reviews.rating) = CAST(
                            AVG(reviews.rating) AS INTEGER)
                         THEN CAST(AVG(reviews.rating) AS INTEGER) ELSE
                         ROUND(AVG(reviews.rating), 2)
                    END AS avg_rating
             FROM recipes, users
             LEFT JOIN reviews
             ON recipes.id = reviews.recipe_id
             WHERE recipes.user_id = users.id
                AND (LOWER(recipes.title)
                        LIKE LOWER(('%') || ? || ('%'))
                    OR LOWER(recipes.ingredients)
                        LIKE LOWER(('%') || ? || ('%'))
                    OR recipes.id IN (
                        SELECT recipe_id
                        FROM classes_in_recipe
                        WHERE LOWER(value) LIKE LOWER(('%') || ? || ('%'))))
             GROUP BY recipes.id
             ORDER BY recipes.id DESC
             LIMIT ?"""
    return db.query(sql, [query, query, query, page_size])
