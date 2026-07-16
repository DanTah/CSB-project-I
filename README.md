# Recipes

## About the project
This is my first project for Helsinki university course "Cyber Security Base". The web application has five security flaws, and except for CSRF, the flaws are taken from OWASP Top Ten 2017 list:
* SQL injection
* XSS
* CSRF
* Broken Access Control
* Broken Authentication

The starter template for this project is taken from another web application, created for the course "Databases and Web Programming" (https://github.com/DanTah/reseptit). 
Note that while some parts of the application remain untranslated, the necessary functionalities and texts are in english for testing the security flaws above.

Note for the peer-reviewers: Microsoft Word's spell checker feature was used to check the spelling of the report.

## Functionalities of the Application

* User can create an account and log into the application.
* User can add, update and remove their own recipes.
* User can check out recipes added by others.
* User can search recipes with a keyword.
* User has their own page where their recipes are listed.
* User can give grade and a comment on their and others' recipes.
* User can update and remove grades and comments they have given.

## Installation Instructions for Testing the Application
Note: If you are a windows user, please use Command Prompt.
Make sure you have Python 3 (version 3.10 or higher is recommended) and SQLite 3 installed.

Clone the repository:
```
git clone https://github.com/DanTah/CSB-project-I.git
```
Navigate to the `CSB-project-I` folder:
```
cd CSB-project-I
```
Create a virtual environment:
* Linux/MacOS:
```
python3 -m venv venv
```
* Windows:
```
python -m venv venv
```

Activate the virtual environment:
* Linux/MacOS:
```
source venv/bin/activate
```
* Windows:
```
venv\Scripts\activate
```
Install `flask` and `bleach`:
```
pip install flask bleach
```
Create the database `database.db` using the file `schema.sql` and insert the data from the file `init.sql`:
```
sqlite3 database.db < schema.sql
sqlite3 database.db < init.sql
```
Execute `seed.py` to initialize the application with some accounts and recipes:
* Linux/MacOS:
```
python3 seed.py
```
* Windows:
```
python seed.py
```
Now you can run the application:
```
flask run
```
