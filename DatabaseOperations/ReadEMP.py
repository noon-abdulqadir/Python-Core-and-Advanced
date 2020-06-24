import mysql.connector

conn = mysql.connector.connect(host="localhost",database="mydb",user="root",password="xxxx")

if conn.is_connected():
    print("Connected to MySQL db.")

    cursor = conn.cursor()
    
    cursor.execute('select * from emp')
    
    row = cursor.fetchone()
    
    while row is not None:
        print(row)
        row = cursor.fetchone()
    
    cursor.close()
    conn.close()

##############################################################################################

import mysql.connector

conn = mysql.connector.connect(host="localhost",database="mydb",user="root",password="xxxx")

if conn.is_connected():
    print("Connected to MySQL db.")

    cursor = conn.cursor()
    
    cursor.execute('select * from emp')
    
    rows = cursor.fetchall()
    print("Total number of records: ",cursor.rowcount)
    
    for row in rows:
        print(row)
    
    cursor.close()
    conn.close()