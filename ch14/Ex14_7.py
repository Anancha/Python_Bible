import pymysql

con = pymysql.connect(host="localhost", database="testmariadb", user="root", password="", charset="utf8")

try :
    cur = con.cursor()
    cur.execute("UPDATE customer SET province = 'กรุงเทพฯ' WHERE province = 'กทม.'")

    con.commit()
    print("ปรับปรุงข้อมูลลูกค้าสำเร็จแล้ว")

    cur.close()
except :
    con.rollback()
    print("ไม่สามารถปรับปรุงข้อมูลในตารางข้อมูลได้")
finally :
    con.close()