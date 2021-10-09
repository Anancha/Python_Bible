import pymysql

con = pymysql.connect(host="localhost", database="testmariadb", user="root", password="", charset="utf8")

try :
    cur = con.cursor()
    cur.execute("DELETE FROM customer WHERE cust_id = 3")

    con.commit()
    print("ลบข้อมูลลูกค้าสำเร็จแล้ว")

    cur.close()
except :
    con.rollback()
    print("ไม่สามารถลบข้อมูลในตารางข้อมูลได้")
finally :
    con.close()