import mysql.connector
import OpenSSL.crypto

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

def fetch_data():
    sql_select_Query = "select * from cars"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    for row in records:
        print("carID =", row[0])
        print("name =", row[1])

def readfile():
    file1 = open("private.key", "r")
    string  = file1.read()
    #print("string : ",string)
    add_data(8, string)
    file1.close()

def readx509Certificate():
    certFile = open("selfsigned.crt").read()
    c = OpenSSL.crypto
    cert = c.load_certificate(c.FILETYPE_PEM, certFile)


    privatekeyFile = open("private.key").read()
    key = c.load_privatekey(c.FILETYPE_PEM, privatekeyFile)
    print(key)

    context = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_METHOD)
    context.use_privatekey(key)
    context.use_certificate(cert)
    try:
        context.check_privatekey()
        print("matches for subject name :",cert.get_subject())
    except OpenSSL.SSL.Error:
        print(OpenSSL.SSL.Error)
readx509Certificate()

#readfile()

#add_data(8, )

#fetch_data()


connection.close()
