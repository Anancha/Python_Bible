from pymongo import MongoClient

client = MongoClient("localhost",27017)

try :
    db = client["testmongodb"]
    for doc in db.customer.find({"province": "กทม."}):
        print(doc,"\n")
        
except :
    print("ไม่สามารถค้นหาข้อมูลได้")