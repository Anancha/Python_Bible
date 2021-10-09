import openpyxl as xl

myCustomer = [["ชื่อ","นามสกุล","เบอร์โทรศัพท์","อีเมล","Line ID"],
              ["แพรวพรรณ","วรรณากุล","0829954499","praewpan@gmail.com","iampraew"],
              ["สมชาย", "ไม้เมือง", "0894254355", "somchai@yahoo.com", "msomchai"],
              ["กุลชาติ", "เมืองยิ่ง", "0819876543", "kulachart@hotmail.com", "kulkul"],
              ["สมใจ", "รักธรรม", "0654457788", "somjai@gmail.com", "somjaija"],
              ["สมศรี", "สุขใจ", "0614224221", "somsri@gmail.com", "sukjai_somsri"]]

file = xl.Workbook()
file.save("custexcel.xlsx")
sheet = file.worksheets[0]
sheet.title = "Customer"
r = 1
for cust in myCustomer:
    for i in range(5):
        sheet.cell(row=r, column=i+1).value = cust[i]
    r += 1
file.save("custexcel.xlsx")
print("บันทึกข้อมูลสำเร็จ")