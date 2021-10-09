import pymysql

con = pymysql.connect(host="localhost", database="testmariadb", user="root", password="", charset="utf8")

try :
    cur = con.cursor()
    cur.execute("SELECT cust_id,first_name,last_name FROM customer")

    cust_data = cur.fetchall()
    for i in cust_data :
        print(i)

    cur.close()
except :
    print("ไม่สามารถเรียกดึงข้อมูลจากฐานข้อมูลได้")
finally :
    con.close()