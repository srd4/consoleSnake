import auxiliarFunctions as aux
import sqlite3
import time
import os

def initiate():
    # Creates scores.db file and the 'scores' table.
    connection = sqlite3.connect("score.db")
    cursor = connection.cursor()

    sql_command = "CREATE TABLE scores (time text, date text, score INT, user text);"

    cursor.execute(sql_command)

    connection.commit()
    connection.close()

    return True


def recordScore(score, user):
    # Inserts new score into database.

    if user == "":
        user = "None"

    pomData = (time.strftime("%H:%M:%S"), time.strftime("%d/%m/"), score, user)

    connection = sqlite3.connect("score.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO scores VALUES (?,?,?,?)",pomData)

    connection.commit()
    connection.close()

    return True


def getScores():
    if not os.path.exists("score.db"):
        initiate()

    connection = sqlite3.connect("score.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * from scores")
    scores = cursor.fetchall()
    connection.close()

    return scores

def highestScores(n=10):
    # Returns list of n highest scores registered.
    scores = getScores()
    scores.sort(key = aux.third, reverse = True)

    if len(scores) == 0:
        return [0]
    return scores[:n]


