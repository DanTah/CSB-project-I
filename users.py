import db
from werkzeug.security import generate_password_hash, check_password_hash
def get_user(user_id):
    sql = """SELECT id, username
             FROM users
             WHERE id = ?"""
    if db.query(sql, [user_id]):
        return db.query(sql, [user_id])[0]
    return None

def get_recipes(user_id):
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
             WHERE recipes.user_id = users.id AND users.id = ?
             GROUP BY recipes.id
             ORDER BY recipes.id DESC"""
    return db.query(sql, [user_id])

def create_user(username, password):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])

def check_login(username, password):
    sql = """SELECT id, password_hash
             FROM users
             WHERE username = ?"""
    result = db.query(sql, [username])
    if not result:
        return None
    result = result[0]
    user_id = result["id"]
    password_hash = result["password_hash"]
    if check_password_hash(password_hash, password):
        return user_id
    return None
