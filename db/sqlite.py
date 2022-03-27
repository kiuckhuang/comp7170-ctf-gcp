import sqlite3


#
# Establishing connection
#

# open a SQLite connection
# a database file called data.db will be created,
# if it does not exist
connection = sqlite3.connect('data.db')

# create a database cursor
cur = connection.cursor()

#
# Creating the table
#

# create the database table if it doesn't exist
table_schema = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
"""
cur.execute(table_schema)

#
# Inserting to the database
#

user1 = 'mary'
pass1 = '33U9VRn,y~[h]Nkv'

user2 = 'john'
pass2 = 'uG4dsM.E-2q!gfn'


# insert some hard-coded data
insert_query = """
INSERT INTO users (username, password) VALUES (?, ?);
"""
#cur.execute(insert_query, (user1, pass1))
#cur.execute(insert_query, (user2, pass2))
# save it in the database file
#connection.commit()

#
# Querying the database
#

# query the database for ALL data in the notes table
cur.execute('SELECT * FROM users;')

# print the result
print('\nUsers:')
for row in cur.fetchall():
    print(row)
#
# Cleaning up
#

# close the cursor
cur.close()

# close the connection
connection.close()