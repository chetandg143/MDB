import pymongo
import json
myclient = pymongo.MongoClient("mongodb://192.168.1.96/")
mydb =myclient['test']
coll = mydb['student']


# f1 = open("student.json","r")
# record = json.load(f1)
# print("inserted successfully ")
# x =coll.insert_many(record)
#

#
# x =coll.find({},{"_id":0, "Name":1 , "Color":1,"Crush":1}).limit(5)
# for y in x:
#     print(y)
# #
#
# myquery ={"Name":{ "$regex": "^S" } }
# a =coll.find(myquery)
# for b in a:
#     print(b)


x = coll.find({} ,{ "_id":0 ,"Name":1})
for y in x:
    print(y)