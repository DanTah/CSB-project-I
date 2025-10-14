CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    recipe_time INTEGER,
    ingredients TEXT,
    instructions TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value TEXT
);

CREATE TABLE classes_in_recipe (
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes,
    title TEXT,
    value TEXT
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes,
    user_id INTEGER REFERENCES users,
    rating INTEGER,
    comment TEXT,
    date DATE
);
