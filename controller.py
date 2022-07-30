import sqlite3 as sql
from unittest import result
import os.path

location = os.path.dirname(os.path.abspath(__file__))

def createDB():
	conn = sql.Connection(location + "/usuarios.db")
	conn.commit()

def createTable():
	conn = sql.Connection(location + "/usuarios.db")
	cursor = conn.cursor()
	cursor.execute(
		"""
		CREATE TABLE user(
			username text,
			password text
		)
		"""
	)
	conn.commit()

def insertRow(username, password):
    conn = sql.Connection(location + "/usuarios.db")
    cursor = conn.cursor()
    query1 = f"INSERT INTO user VALUES ('{username}', '{password}')"
    cursor.execute(query1)
    conn.commit()
    conn.close()

def verifyReg(user):
    ans = False
    conn = sql.Connection(location + "/usuarios.db")
    cursor = conn.cursor()
    query1 = f"SELECT username FROM user WHERE username = '{user}'"
    rows = cursor.execute(query1)
    result = rows.fetchall()
    if len(result) == 0:
        ans = True
    conn.commit()
    conn.close()
    return ans

def verifyLog(user, passw):
    ans = False
    conn = sql.Connection(location + "/usuarios.db")
    cursor = conn.cursor()
    query1 = f"SELECT username, password FROM user WHERE username = '{user}' AND password = '{passw}'"
    rows = cursor.execute(query1)
    result = rows.fetchall()
    if len(result) >= 1:
        ans = True
    conn.commit()
    conn.close()
    return ans

if __name__ == "__main__":
    pass
    #insertRow("santicr", "santi8590")
    #createTable()
    #createDB()