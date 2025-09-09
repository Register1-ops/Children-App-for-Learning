import tkinter as tk
import sqlite3
import Login


def storeResults(countWrong, countCorrect, QuizType, wrongQuestionsID, TheirAnswer):
        userID = Login.getUserID() # gets the userID of the user that has logged in
        conn = sqlite3.connect("address_book.db")  # connects to the address book database
        cursor = conn.cursor()  # allows a cursor to be used so items can be accessed from the database
        cursor.execute(f"""SELECT COUNT(*)
                    FROM results
                    WHERE userID = ? AND  QuizType = ?
                    """, (userID, QuizType))
        # completes the query where it selects every field from the results table where a given userId
        # and quizType are given

        row = cursor.fetchone() # it only fetches one row, since there may be many rows of data that have been accessed
        attemptNo = row[0]+1 # obtains the zeroth index of the row, since there will be many values that are
        # stored in one tuple, the attempt N0. is incremented by 1.
        percentage = (countCorrect/(countWrong+countCorrect))*100 # calculates the percentage of right answers
        percentage = round(percentage,2) # round the percentage to 2 decimals places

        cursor.execute(f"""INSERT INTO results
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                            """, (userID, countWrong, countCorrect, percentage, attemptNo, QuizType,
                                  ",".join([str(x) for x in wrongQuestionsID]), ",".join([str(x) for x in TheirAnswer])))
        # executes a query

        conn.commit()  # this commits the changes to the database that have been made, if there have been any changes
        conn.close()  # closes the database so that it cant be edited and changed


def getResults(QuizType):
        userID = Login.getUserID() # gets the userID of the user that has logged in
        conn = sqlite3.connect("address_book.db")  # connects to the address book database
        cursor = conn.cursor()  # allows a cursor to be used so items can be accessed from the database
        cursor.execute(f"""SELECT WrongQuestionsID, TheirAnswer, percentageCorrect
                        FROM results
                        WHERE userID = ? AND QuizType = ?
                        ORDER BY attemptNo
                        """, (userID, QuizType))

        # this query sects the WrongQuestionsID and TheirAnswer from the results table where a userID and Quizype are
        # given, this is then ordered by attemptNo which is stored as an integer

        rows = cursor.fetchall()  # this fetches all of the rows that have been obtained from the database

        PastAttempts = [[int(y) for y in x[0].split(",") if len(y) > 0] for x in rows]
        Answers = [[int(y) for y in x[1].split(",") if len(y) > 0] for x in rows]
        # nested list comprehensions with a condition
        # for x in rows, which has the set of WrongQuestionsID, TheirAnswer, percentageCorrect
        #

        PercentageCorrect = [row[2] for row in rows]
        return PastAttempts, Answers, PercentageCorrect
