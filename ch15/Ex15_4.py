from pymongo import MongoClient

client = MongoClient("localhost",27017)

try :
    db = client["testmongodb"]
    print(db.customer.find_one({"cust_id":2}))

except :
    print("ไม่สามารถค้นหาข้อมูลได้")