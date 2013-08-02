import sys
import sqlite3
import datetime 


createDb = sqlite3.connect(':memory:')
# memory is a placeholder currently



if len(sys.argv) == 1:
    #We are in the interpreter mode.
    print "We are in the interpreter mode."
    #TODO:All of the code here will do the interpreting.

    movie = raw_input('Enter a movie title:')
    date = raw_input('Enter a date d/m/y:')
    rate = raw_input('Please enter a number 1-10:')
    # For an IF statement to run indentation matters.

else:
    print "We are in the command line mode."
    #TODO:All of the code here to parse the arguments.
