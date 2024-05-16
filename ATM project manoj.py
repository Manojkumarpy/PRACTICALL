import mysql.connector
a = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin")

mycursor = a.cursor()
mycursor.execute("create database emp