from pymongo import MongoClient

client = MongoClient("localhost",27017)

try :
    db = client["testmongodb"]
    for doc in db.customer.find() :
        print(doc)

except :
    print("ไม่สามารถค้นหาข้อมูลได้")