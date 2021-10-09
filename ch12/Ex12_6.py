import csv

with open("custcontact.csv", "w" , encoding="UTF-8" , newline = "") as csvfile :
    custcontact_writer = csv.writer(csvfile)
    custcontact_writer.writerow(["ชื่อ","นามสกุล","เบอร์โทรศัพท์","อีเมล","Line ID"])
    custcontact_writer.writerow(["แพรวพรรณ","วรรณากุล","0829954499","praewpan@gmail.com","iampraew"])
    custcontact_writer.writerow(["สมชาย", "ไม้เมือง", "0894254355", "somchai@yahoo.com", "msomchai"])
    custcontact_writer.writerow(["กุลชาติ", "เมืองยิ่ง", "0819876543", "kulachart@hotmail.com", "kulkul"])
    custcontact_writer.writerow(["สมใจ", "รักธรรม", "0654457788", "somjai@gmail.com", "somjaija"])
    custcontact_writer.writerow(["สมศรี", "สุขใจ", "0614224221", "somsri@gmail.com", "sukjai_somsri"])

