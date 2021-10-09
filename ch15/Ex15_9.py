from pymongo import MongoClient

client = MongoClient("localhost",27017)

try :
    db = client["testmongodb"]
    
    print("ก่อนปรับปรุงข้อมูล")
    for doc in db.customer.find({"province": "กทม."}) :
        print(doc)

    
    # ทำการปรับปรุงข้อมูล
    criteria = { "province": "กทม." }
    update_data = { "$set": { "province": "กรุงเทพมหานคร" } }

    db.customer.update_many(criteria,update_data)
    
    print("หลังปรับปรุงข้อมูล")
    for doc in db.customer.find({"province": "กรุงเทพมหานคร"}) :
        print(doc)
    
except :
    print("ไม่สามารถปรับปรุงข้อมูลได้")