
import pymongo
import json

myclient = pymongo.MongoClient("mongodb://192.168.1.96/")
mydb = myclient['test']
coll = mydb['jsondata']

# file =open("fire.json","r")
# data = json.load(file)
# print("inserted all data into mongodb")
# x = coll.insert_many(data)


# query ={"person":"Guru"}
# a = coll.delete_one(query)
# print(a.deleted_count)

x = coll.find({},{"_id":0 })
for y in x:
    print(y)
