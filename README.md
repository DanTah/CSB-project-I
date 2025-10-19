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

## Asennusohjeet sovelluksen testaamiseksi
Kloonaa repositorio:
```
git clone https://github.com/DanTah/reseptit.git
```
Siirry kansioon `reseptit`:
```
cd reseptit
```
Asenna `flask` -kirjasto:
```
pip install flask
```
Luo tiedoston `schema.sql` avulla tietokanta tiedostoon `database.db` ja lisää tiedoston `init.sql` tiedot:
```
sqlite3 database.db < schema.sql
sqlite3 database.db < init.sql
```
Nyt voit käynnistää sovelluksen:
```
flask run
```
