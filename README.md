# reseptit

## Sovelluksen toiminnot

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan omia ruokareseptejä.
* Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan reseptinsä kuvan.
* Käyttäjä näkee sovellukseen lisätyt reseptit.
* Käyttäjä pystyy etsimään reseptejä hakusanalla.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät käyttäjän lisäämät reseptit ja lisäysten lukumäärän.
* Käyttäjä pystyy valitsemaan lisäämälleen reseptille yhden tai useamman luokittelun (esim. gluteiiniton, pääruoka, intialainen, ...).
* Käyttäjä pystyy antamaan jokaiselle sovellukseen reseptille kommentin ja arvosanan. Reseptistä näytetään kommentit sekä arvosanat ja niiden keskiarvo.
* Käyttäjä pystyy muokkaaamaan ja poistamaan antamiaan kommentteja ja arvosanoja.

## Installation Instructions for Testing the Application
Clone the repository:
```
git clone https://github.com/DanTah/reseptit.git
```
Navigate to the `reseptit` folder:
```
cd reseptit
```
Install the `flask` library:
```
pip install flask
```
Create the database `database.db` using the file `schema.sql` and insert the data from the file `init.sql`:
```
sqlite3 database.db < schema.sql
sqlite3 database.db < init.sql
```
Now you can run the application:
```
flask run
```
## Sovelluksen toiminta suurella tietomäärällä
Sovelluksen tietokantaan on luotu testiaineisto ajamalla `seed.py`, jolloin käyttäjien määrä on
100000, reseptien määrä on 1000000 ja arvioiden määrä on 10000000. 

Sovelluksen nopeutta on aluksi testattu tapauksessa, missä tietokantaan ei ole lisätty indeksejä `idx_user_recipes` ja `idx_recipe_reviews`. Alla on esitetty etusivun reseptilistan viiden ensimmäisen sivun latausnopeudet:
```
elapsed time: 28.42 s
127.0.0.1 - - [19/Oct/2025 21:26:11] "GET / HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [19/Oct/2025 21:26:11] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 27.76 s
127.0.0.1 - - [19/Oct/2025 21:27:01] "GET /2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [19/Oct/2025 21:27:01] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 27.61 s
127.0.0.1 - - [19/Oct/2025 21:27:33] "GET /3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [19/Oct/2025 21:27:33] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 27.47 s
127.0.0.1 - - [19/Oct/2025 21:28:14] "GET /4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [19/Oct/2025 21:28:14] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 27.54 s
127.0.0.1 - - [19/Oct/2025 21:28:51] "GET /5 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [19/Oct/2025 21:28:51] "GET /static/main.css HTTP/1.1" 304 -
```

Lisäämällä edellä mainitut indeksit tietokantaan latausnopeus paranee huomattavasti:
```
elapsed time: 0.04 s
127.0.0.1 - - [19/Oct/2025 21:36:31] "GET / HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [19/Oct/2025 21:36:31] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.04 s
127.0.0.1 - - [19/Oct/2025 21:36:36] "GET /2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [19/Oct/2025 21:36:36] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.03 s
127.0.0.1 - - [19/Oct/2025 21:36:37] "GET /3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [19/Oct/2025 21:36:37] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.04 s
127.0.0.1 - - [19/Oct/2025 21:36:39] "GET /4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [19/Oct/2025 21:36:39] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.04 s
127.0.0.1 - - [19/Oct/2025 21:36:40] "GET /5 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [19/Oct/2025 21:36:40] "GET /static/main.css HTTP/1.1" 304 -
```
