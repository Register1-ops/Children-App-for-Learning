import sqlite3  # importing sql, to allow access to sql language to access database created


 

class database():

    def __init__(self):
        
    
        # create a database or connect to one
        conn = sqlite3.connect("address_book.db") #  connecting to a databse called addresss book
        # create a cursor
##        cursor = conn.cursor()
##        conn.execute("""CREATE TABLE addresses(
##                first_name text,
##               second_name text
##                )""")

        conn.execute("""CREATE TABLE users(
                userID INTEGER PRIMARY KEY,
                FirstName Text,
                Surname Text,
                username TEXT UNIQUE,
                password BLOB,
                salt TEXT
                )""")   # executes creating a table called users with different records, such as user ID
                        # username
                        # password
                        # salt
                        # all with different data types based on what they may type
        # BLOB = unstructured binary data, can be anything         
        # commit change
        conn.commit()
        # close connection
        conn.close()   # closes the database so it cant be accidentaly erased, or modified or deleted

#database()


