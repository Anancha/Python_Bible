from pymongo import MongoClient

client = MongoClient("localhost",27017)

try :
    db = client["testmongodb"]
    
    doc = {"cust_id": 5,
            "first_name": "วีระ",
            "last_name": "รักธรรม",
            "phone": "0893345687",
            "street": "12 ต.บางพลีใหญ่",
            "city": "บางพลี",
            "province": "สมุทรปราการ",
            "zipcode": "10540"}
    
    db.customer.insert_one(doc)
    
    print("เพิ่มข้อมูลเรียบร้อยแล้ว")
    for search_doc in db.customer.find() :
        print(search_doc)
    
except :
    print("ไม่สามารถเพิ่มข้อมูลได้")