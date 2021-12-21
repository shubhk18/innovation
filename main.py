import mysql.connector

username = "root"
password = "mypass"

connection = mysql.connector.connect(
    user=username,
    password=password,
    host="localhost",
    port="3306",
    database="mydb")

if connection.is_connected():
    print("Connected")
else:
    print("Not connected")

cursor = connection.cursor()


def add_data(id, CarName):
    statement = "INSERT INTO cars (carID,name) VALUES (%s, %s)"
    data = (id, CarName)
    cursor.execute(statement, data)
    connection.commit()
    print("Successfully added entry to database")


add_data(6, "KIA sonnet")

connection.close()
