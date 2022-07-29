import sqlite3 as sql

def createDB():
	conn = sql.connect("usuarios.db")
	conn.commit()
	conn.close()

def createTable():
	conn = sql.connect("usuarios.db")
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
	conn.close()

def insertRow(username, password):
    conn = sql.connect("usuarios.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO usuarios VALUES ({username}, {password})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def verifyRow(username):
    ans = False
    conn = sql.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT username FROM user WHERE (username = {username})"
    )
    result = cursor.fetchall()
    if len(result) == 0:
        ans = True
    conn.commit()
    conn.close()
    return ans

if __name__ == "__main__":
    createTable()
    #createDB()