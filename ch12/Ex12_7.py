import csv

myCustomer = [["ชื่อ","นามสกุล","เบอร์โทรศัพท์","อีเมล","Line ID"],
              ["แพรวพรรณ","วรรณากุล","0829954499","praewpan@gmail.com","iampraew"],
              ["สมชาย", "ไม้เมือง", "0894254355", "somchai@yahoo.com", "msomchai"],
              ["กุลชาติ", "เมืองยิ่ง", "0819876543", "kulachart@hotmail.com", "kulkul"],
              ["สมใจ", "รักธรรม", "0654457788", "somjai@gmail.com", "somjaija"],
              ["สมศรี", "สุขใจ", "0614224221", "somsri@gmail.com", "sukjai_somsri"]]

with open("custcontact2.csv", "w" , encoding="UTF-8" , newline = "\n") as csvfile :
    custcontact_writer = csv.writer(csvfile)
    custcontact_writer.writerows(myCustomer)