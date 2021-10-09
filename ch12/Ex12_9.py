import csv

with open("custcontact.csv", "r") as csvfile :
    custcontact_reader = csv.DictReader(csvfile)
    for mycust in custcontact_reader :
        print(mycust)
        #print(mycust["ชื่อ"], mycust["นามสกุล"], mycust["เบอร์โทรศัพท์"], mycust["อีเมล"], mycust["Line ID"])