import mysql.connector

# Setup DB connection
def get_db_connection():
    return mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Dama@1122",
    database="dbms"
)
