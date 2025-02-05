import sqlite3 as sqlite

#open a connection to a database called 'database.db'
connection = sqlite.connect('database.db')

#use the open function to open the schema.sql file (created in project)
with open('schema.sql') as f:
    #use the executescript function that will execute multiple sql scripts
    connection.executescript(f.read())

#create a cursor object so we can use the execute method to execute two INSERT sql statements to add two posts to the posts table
cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?,?)",
('First Post', 'first post content')
)

cur.execute("INSERT INTO posts (title, content) VALUES (?,?)",
('Second Post', 'second post content')
)

#this commits the changes to the connection, then closes the connection
connection.commit()
connection.close()
