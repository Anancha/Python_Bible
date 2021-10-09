from pymongo import MongoClient

client = MongoClient("localhost",27017)

try :
    db = client["testmongodb"]
    
    criteria = { "cust_id": 1 }
    db.customer.delete_one(criteria)
    
    print("ลบข้อมูลของรายการ cust_id = 1 สำเร็จ")
    for doc in db.customer.find() :
        print(doc)

except :
    print("ไม่สามารถลบข้อมูลได้")