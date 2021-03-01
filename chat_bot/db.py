import mysql.connector
from mysql.connector import Error

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='vk_chatbot_db'
)
#print(my_db)

my_cursor = my_db.cursor()

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


#my_cursor.execute('CREATE DATABASE vk_chatbot_db')

#my_cursor.execute('CREATE TABLE merchandise (categories VARCHAR(255), products VARCHAR(255))')

sqlFormula = 'INSERT INTO merchandise (categories, products) VALUES(%s, %s)'
merch1 = ('кондитерские изделия', 'печенье')
merch2 = ('кондитерские изделия', 'пряник')
merch3 = ('мучные изделия без начинки', 'крендель')
merch4 = ('мучные изделия без начинки', 'слойка')
merch5 = ('пирожки', 'пирожок с яйцом и зеленью')
merch6 = ('пирожки', 'пирожок с мясом')
#my_cursor.execute(sqlFormula, merch6)
#my_db.commit()
