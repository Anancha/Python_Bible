from pymongo import MongoClient

client = MongoClient("localhost",27017)

try :
    db = client["testmongodb"]
    
    doc = [
           {"cust_id": 6,
            "first_name": "ชูใจ",
            "last_name": "สวัสดิรักษา",
            "phone": "0871122333",
            "street": "12 ม.3 ซ.เทศบาล 9 ต.พิมลราช",
            "city": "บางบัวทอง",
            "province": "นนทบุรี",
            "zipcode": "11110"},
           {"cust_id": 7,
            "first_name": "มานี",
            "last_name": "สว่างธรรม",
            "phone": "0869988777",
            "street": "98/89 ซ.แจ้งวัฒนะ 10 ทุ่งสองห้อง",
            "city": "หลักสี่",
            "province": "กทม.",
            "zipcode": "10210"},
           {"cust_id": 8,
            "first_name": "สีดา",
            "last_name": "สายบัวทอง",
            "phone": "0893345678",
            "street": "9/157 ถ.เชิดวุฒากาศ",
            "city": "ดอนเมือง",
            "province": "กทม.",
            "zipcode": "10210"},
          ]
    
    db.customer.insert_many(doc)
    
    print("เพิ่มข้อมูลเรียบร้อยแล้ว")
    for search_doc in db.customer.find({"cust_id": {"$gt":5}}) :
        print(search_doc)
    
except :
    print("ไม่สามารถเพิ่มข้อมูลได้")