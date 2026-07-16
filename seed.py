import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM recipes")
db.execute("DELETE FROM classes_in_recipe")
db.execute("DELETE FROM reviews")

SQL = "INSERT INTO users (id,username, password_hash) VALUES (?,?,?)"

db.execute(SQL, [1,'user1', 'password1'])
db.execute(SQL, [2,'bad_user', 'password2'])
db.execute(SQL, [5,'uncertain_user','seeme?'])

db.commit()

SQL = "INSERT INTO recipes (title, recipe_time, ingredients, instructions, user_id, image) VALUES (?,?,?,?,?,?)"
db.execute(SQL, ["User1's Rrecipe", 3, '-', '-', 1, None])
db.execute(SQL, ["bad_recipe", 1, '1', '1', 2, None])

db.commit()

SQL = "INSERT INTO reviews (recipe_id, user_id, rating, comment, date) VALUES (?,?,?,?,?)"
db.execute(SQL, [1, 1, 5, 'Perfect recipe for christmas!!!', '29.10.2025'])
db.execute(SQL, [1, 2, 1, 'bad comment', '29.10.2025'])

db.commit()
db.close()
