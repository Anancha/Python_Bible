from pymongo import MongoClient

client = MongoClient("localhost",27017)

try :
    db = client["testmongodb"]
    
    db.customer.delete_many({})
    
    print("ลบข้อมูลทุกรายการสำเร็จ")
    for doc in db.customer.find() :
        print(doc)

except :
    print("ไม่สามารถลบข้อมูลได้")
