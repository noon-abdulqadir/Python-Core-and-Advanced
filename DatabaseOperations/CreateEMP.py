import mysql.connector

conn = mysql.connector.connect(host="localhost",database="mydb",user="root",password="xxxx")

if conn.is_connected():
    print("Connected to MySQL db.")

    cursor = conn.cursor()
    
    cursor.execute('select * from emp')
    
    try:
        cursor.execute('insert into emp values(2,"Noon",30000)')
        conn.commit()
        print("Employee Added.")
    except:
        conn.rollback()

    cursor.close()
    conn.close()