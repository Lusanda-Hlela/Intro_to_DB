import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
	try:
		cursor.execute("CREATE DATABASE alx_book_store")
		print("Database 'alx_book_store' created successfully!")
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_DB_CREATE_EXISTS:
			print("Database 'alx_book_store' already exists.")
		else:
			print(f"Failed to create database: {err.msg}")


def main():
	try:
		# Establish connection to MySQL server
			conn = mysql.connector.connect(
					user="lusanda",
					password="Man8244251",
					host="localhost",
			)

			cursor = conn.cursor()
			create_database(cursor)

	except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
					print("Error: Access denied - invalid username or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
					print("Error: Database does not exist")
			else:
					print(f"Error: {err}")

	finally:
			# Close the cursor and connection
			cursor.close()
			conn.close()

if __name__ == "__main__":
	main()