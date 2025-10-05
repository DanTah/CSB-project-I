import db

def get_user(user_id):
    sql = """SELECT id, username
             FROM users
             WHERE id = ?"""
    if db.query(sql,[user_id]):
        return db.query(sql,[user_id])[0]
    return None

def get_recipes(user_id):
    sql = """SELECT id, title
             FROM recipes
             WHERE user_id = ?
             ORDER BY id"""
    return db.query(sql,[user_id])
