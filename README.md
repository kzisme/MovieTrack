MovieTrack
==========

I've been thinking about the basic functionality of the program and essentially it will have three main functions.  It will...1. Take user input which will consist of movie title,date viewed, Rating 1-10 (either using numbers or printing out ASCII symbols/10.  

All of the user input will be stored using SQLite and I'm planning on getting the GUI manager since it seems a little easier. (Unless it's simple in CLI in Ubuntu).  When adding a new movie the program will first ask the user for a movie title then they will be told to hit the return key.  The same thing will happen for the date and rating inputs.  Once the user has completed all of the required fields to add a movie the program will print something like "Your movie has been added successfully.  You you like to add another Y/N"

Since at my current position adding a GUI seems a little complicated so there would have to be a way for the user to actually view their movies they have watched.  When the program is first ran There will be a list of options consisting of something like "Add Movie, Edit Rating, List(Print out list of movies,dates and ratings), and Help.  I don't see a reason to include a delete function because the programs purpose is to remember movies you have seen.  The other two functions are self explanatory.  

I'm not terribly sure about what libraries should be used to make this project come to life or really where to start with everything, or if all of these ideas are feasible or worth adding into the program.

As for future additions...I suppose I could add something that could track the price you paid for a movie ticket or the DVD.  I don't think it would complex to instead print the information from the database to a table on a website that fits to the data.  If that was possible I suppose we could also add a column if the user owns the movie or not.  I think it would feasible to also rip DVD pictures to add into a column too at some point.  It could rip the default movie image from a movie's IMDB page or something (this is my "out there" idea).
