import mysql.connector

def delete(id):
    conn = mysql.connector.connect(host="localhost",database="mydb",user="root",password="xxxx")

    if conn.is_connected():
        print("Connected to MySQL db.")
    
        cursor = conn.cursor()
        
        str = "Delete from emp where id = %d"
        args=(id)
        
        try:
            cursor.execute(str % args)
            conn.commit()
            print("Employee Deleted.")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

empid=int(input("Enter emp id: "))
delete(empid)