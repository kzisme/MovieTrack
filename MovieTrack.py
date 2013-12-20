import sys
import sqlite3
import datetime
#TO-DO:
#Fix a few user options...I think like Options 3-5 or something.
#
conn = sqlite3.connect('moviedb.db')
c = conn.cursor()

class Movie(object):
    def __init__(self, db, name, create):
        self.db = db
        self.name = name.lower() #Not sure if I should always format to lower case.
        self.day = day
        self.rating = rating
        if not self.in_db():
            self.create()
        create = False
	@property
   	def all(self):
        	return self.db.c.execute("SELECT * FROM myMovies")

    def delete(self):
        self.db.c.execute("DELETE FROM myMovies WHERE movie == ?", (self.name,))
        conn.commit()

    def in_db(self):
        self.db.c.execute("SELECT * FROM myMovies WHERE movie == ?", (self.name,))
        try:
            self.db.c.fetchone()
            return True
        except sqlite3.DatabaseError:
            return False

    def create(self):
        self.db.c.execute("INSERT INTO myMovies (movie, day, rating) VALUES (?, ?, ?) ", (self.name, self.day, self.rating))
        conn.commit()

class Actor(object):
    def __init__(self):
        self.name = name
        if not self.in_db():
            self.add_to_db()
        self.db.close()
        print self.name

    def delete(self):
        self.db.c.execute("DELETE FROM actors WHERE actor == ?", (self.name,))
        self.db.conn.commit()

    def in_db(self):
        self.db.c.execute("SELECT * FROM actors WHERE actor == ?", (self.name,))
        try:
            self.db.c.fetchone()
            return True
        except sqlite3.DatabaseError:
            return False

    def add_to_db(self):
        self.db.c.execute("INSERT INTO actors VALUES (?)", (self.name,))

def Rating(object):
    def __init__(self, rating, movie, user):
        self.rating = rating
        self.movie = movie
        self.user = user
        if not self.in_db():
            self.add_to_db()

    def delete(self):
        self.db.c.execute("DELETE FROM ratings WHERE username == ?", (self.user.name,))
        self.db.conn.commit()

    def in_db(self):
        self.db.c.execute("SELECT * FROM ratings WHERE username == ?", (self.user.name,))
        try:
            self.db.fetchone()
            return True
        except sqlite3.DatabaseError:
            return False

    def add_to_db(self):
        self.db.c.execute("INSERT INTO ratings VALUES (?)", (self.user.name,))  # I'm not sure if this syntax is right; I just tried it. No guarantees.

    def get_all_by_user(self):
        self.db.c.execute("SELECT movie, date, rating FROM ratings WHERE username == ?", (self.user.name,))
        return self.db.c.fetchall()

class User(object):
    def __init__(self, db, username, password):
        self.db = db
        self.username = username
        self.password = password
        self.movies_viewed = self.get_viewed_movies()

    def get_viewed_movies(self):
        self.db.c.execute("SELECT movie, date, rating FROM viewed_movies WHERE username='%s'" % self.username)
        row = c.fetchone()
        row = (1, 2, 3) # replace with db fetch
        if None in row:
             return None
        return dict(zip(('movie', 'date', 'rating'), row))



class Database(object):
    def __init__(self, file):
        self.db = sqlite3.connect(file)
        self.c = self.db.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS movies
                (movie text)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
                (username text, password text)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS viewed_movies
                (movie text, date text, username text, rating text)''')

    def __del__(self):
        self.db.commit()  # When the program closes, shit gonna commit.

if __name__ == "__main__":
    db = Database("moviedb.db")
    u = raw_input("Username: ")
    p = raw_input("Password: ")
    user = User(db, u, p)  # So we have the user object. Now we want to get the current movies from it right away to save calls later.  Or maybe not, let's save it.
    while True:
        print("""
                1. Add a movie.
                2. Delete a movie.
                3. View your ratings.
                4. View all movies.
                5. Rate a movie.

        """)
        option = raw_input("Please select an option:")
        if option == "1":
            movie_name = raw_input('Enter a movie title:')
            day = raw_input('Enter the date you viewed the movie:')
            rating = raw_input('Please enter a rating for you movie 1-10:')
            movie = Movie(db, movie_name, create = True)
            movie.create()
            print("Your movie has been added",)
        elif option == "2":
            to_delete = raw_input("Please type a movie that you want deleted:",)
            day = "" #There is probably a better way to do this...change it later
            rating = "" #There is probably a better way to do this...change it later
            movie = Movie(db, to_delete, create = True)
            if movie is None:
                print("That movie is not in database")
            else:
                movie.delete()
                print("Movie {} has been deleted".format(to_delete))
            print("Your movie has been deleted.",)
        elif option == "3":
            print user.get_viewed_movies()
        elif option == "4":
            print user.movies_viewed
        elif option == "5":
            movie_name = raw_input("Movie name?")
            try:
                movie = Movie(db, movie_name)
                r = raw_input("Rating? (1-10)")
                rating = Rating(db, r, movie, user)
            except:
                print "I didn't handle this properly, I'm still on my bender and I bought a house; give me a break."
        sys.exit(0)
