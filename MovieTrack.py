import sys
import sqlite3
import datetime

createDb = sqlite3.connect('moviedb.db')
conn = sqlite3.connect('moviedb.db')
c = conn.cursor()
#c.execute("DROP TABLE IF EXISTS myMovies")
c.execute('''CREATE TABLE IF NOT EXISTS myMovies
(movie text, day text, rating integer)''')

movie = raw_input('Enter a movie title:')
day = raw_input('Enter a date d/m/y:')
rating = raw_input('Please enter a number 1-10:')

c.execute("insert into myMovies (movie, day, rating) values (?, ?, ?)",
			(movie, day, rating))

conn.commit()