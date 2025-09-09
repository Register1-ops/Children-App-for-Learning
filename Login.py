import sqlite3
import getHashPassword  # imports the getHashPassword module i created

_userID = None # managing how people access the userID, not letting anyone access the userID
# underscore signals to other people don't change it or it will break stuff


class NotLoggedInError(Exception):  # making my own error catcher
    pass


def getUserID():
    if _userID is not None:
        return _userID  # returns the userID, function to manage people accessing the variable
# this is a getter to get the userID

    else:
        raise NotLoggedInError()

def verification(user_name, password): # passes the username and password created by the use
    global _userID # using variable userID which is in the outer scope
    conn = sqlite3.connect("address_book.db") # connects to the address book database
    cursor = conn.cursor() # allows a cursor to be used so items can be accessed from the database
    cursor.execute(f"""SELECT userID, username, password, salt 
    FROM users
    WHERE username = ?
    LIMIT 1
    """, (user_name,))  # selects the user's username, password, salt from the arguments that are passed
    # treat user_name is data not an instruction
    row = cursor.fetchone() # fetches one
    if row: # if one was fetched, so if it was actually in the database
        hashPassword = getHashPassword.getHashPassword(password, row[3])  # this calls the getHashPassword function
        # that passes password that the user has entered and row[3] which is the individual salt that has been appended to the
        # password
        if hashPassword.hex() == row[2]:  # if the hex of the hashPassword which is the password and salt is the same
            # as the password obtained from the database, then
            _userID = row[0]
            # the userId is the userID that the was obtained from the database that related to the the user
            return row[0]
        else: # if it is not equal
            raise NotLoggedInError() # an error that i have coded above called the NotLoggedInError
            # is outputted to the user, so that means that the credentials are not valid
    else:  # if row is false, meaning that there is no field found in the database that has the specific username
        # the user  has entered
        raise NotLoggedInError() # a NotLoggedInError is raised to the user so that they need to sign in
        # instead of logging in

