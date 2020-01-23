import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "leonlee",
    passwd = "lw9717lw",
    database = "spendingdaily"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE spending (types VARCHAR (255), detail VARCHAR (255), price INTEGER)")