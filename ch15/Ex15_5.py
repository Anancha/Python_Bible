from pymongo import MongoClient

client = MongoClient("localhost",27017)

try :
    db = client["testmongodb"]
    print("แสดงข้อมูลลูกค้าที่มีรหัสลูกค้าน้อยกว่าหรือเท่ากับ 3")
    for doc in db.customer.find({"cust_id": {"$lte":3}}):
        print(doc)
    
    print("\nแสดงข้อมูลลูกค้าที่มีรหัสลูกค้าไม่เท่ากับ 1 และลูกค้าอยู่จังหวัด กทม.")
        
    for doc in db.customer.find({"$and": [{"cust_id": {"$ne":1}}, {"province" : "กทม."}]}) :
        print(doc)
    
except :
    print("ไม่สามารถค้นหาข้อมูลได้")