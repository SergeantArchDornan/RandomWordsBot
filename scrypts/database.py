import sqlite3

conn = sqlite3.connect('database/users.db', check_same_thread=False)
cursor = conn.cursor()

def insert(user_name: str, user_password: str):
	cursor.execute('INSERT INTO Users (name, password) VALUES (?, ?)', (user_name, user_password))
	conn.commit()
	
def check(user_name: str, user_password: str):
	query = 'SELECT password FROM Users WHERE name = ?'
	cursor.execute(query, (user_name,))
	real_password = cursor.fetchall()
	if(len(real_password) == 0):
		return False
	if real_password[0][0] == user_password:
		return True
	else:
		return False