
import sqlite3
# create a new database if the database doesn't already exist
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("INSERT INTO population VALUES('New York City', 'NY', 8400000)")
	c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

