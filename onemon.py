import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.1.96/")
mydb = myclient["chets"]
mycol = mydb["EmpRecords"]
print("inserted! ")
mydict = { "name": "Ashok", "address": "Kamakshipalya" ,"city":"Bengaluru"}

x = mycol.insert_one(mydict)
print(mydict)