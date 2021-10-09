from pymongo import MongoClient

client = MongoClient("localhost",27017)

try :
    db = client["testmongodb"]
    
    print("ก่อนปรับปรุงข้อมูล")
    print(db.customer.find_one())
    
    # ทำการปรับปรุงข้อมูล
    criteria = { "cust_id": 1 }
    update_data = { "$set": { "province": "กรุงเทพฯ" } }
    
    db.customer.update_one(criteria,update_data)
    
    print("หลังปรับปรุงข้อมูล")
    print(db.customer.find_one())
    
except :
    print("ไม่สามารถปรับปรุงข้อมูลได้")