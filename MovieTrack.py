import sys
import sqlite3
import datetime

conn = sqlite3.connect('moviedb.db')
c = conn.cursor()

def connect_to_db():
	conn = sqlite3.connect('moviedb.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS myMovies
		movie text, day text, rating integer)''')
	return conn

def add_to_db(movie,day,rating):
	conn = sqlite3.connect('moviedb.db')
	c = conn.cursor()
	c.execute("insert into myMovies (movie, day, rating) values (?, ?, ?)",
		(movie, day, rating))
	conn.commit()

continue_game = True
while continue_game:
	print("""
		1. Add a movie.
		2. Delete a movie.
		3. View entries.
        """)
	option = raw_input("Please select an option:")
	if option == "1":
		movie = raw_input('Enter a movie title:')
		day = raw_input('Enter a date d/m/y:')
		rating = raw_input('Please enter a number 1-10:')
		add_to_db(movie,day,rating)
		print("Your movie has been added")
	elif option == "2":
		print("Your movie has been deleted.")
	elif option == "3":
		rows = c.fetchall()
		for row in rows:
			print row
	elif option == "":
		sys.exit(0)

conn.commit()
