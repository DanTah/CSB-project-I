import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM recipes")
db.execute("DELETE FROM classes_in_recipe")
db.execute("DELETE FROM reviews")

user_count = 10**5
recipe_count = 10**6
review_count = 10**7

for i in range(1, user_count + 1):
    db.execute("INSERT INTO users (username) VALUES (?)",
               ["user" + str(i)])

for i in range(1, recipe_count + 1):
    title = "test"+str(i)
    recipe_time = 1
    ingredients ="ingredient"
    instructions ="instructions"
    user_id = random.randint(1,user_count)
    image = None
    sql = """INSERT INTO recipes (title, recipe_time, ingredients,
                                  instructions, user_id, image)
             VALUES (?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [title, recipe_time, ingredients,
                     instructions, user_id, image])

for i in range(1, review_count + 1):
    recipe_id = random.randint(1, recipe_count)
    user_id = random.randint(1, user_count)
    rating = 5
    comment = "comment"+str(i)
    db.execute("""INSERT INTO reviews (recipe_id, user_id, rating, comment, date)
                  VALUES (?, ?, ?, ?, datetime('now'))""",
               [recipe_id, user_id, rating, comment])

db.commit()
db.close()




