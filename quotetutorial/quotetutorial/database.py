import sqlite3

conn = sqlite3.connect('myquotes.db') # Creating a connection variable for creating and connecting databases
curr = conn.cursor()                  # Create Cursor varibale that help us to take advantage of all the other functionalities  that are inside this sqlite3 package

# Creating a table inside our sqlite3 database ("""""") using for writing multiples queries

# curr.execute(""" create table quotes_tb(
#                  title text,
#                  author text,
#                  tag text
#                  )""")

# Now inserting the values in the fields
curr.execute("""insert into quotes_tb values ('Python is awesome!','buildwithpython', 'Python')""")

# Commit is used to push all the work into myquotes.db
conn.commit()
conn.close()
