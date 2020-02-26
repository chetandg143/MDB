

import  pymongo

myclient  =pymongo.MongoClient("mongodb://192.168.1.96/")
mydb = myclient['test']
mycol = mydb['customers']

mydoc = mycol.find({} ,{"_id":0 ,"address":0}).sort("name")
print("Ascending order\n")
for x in mydoc:
    print(x)
print("\n")
print("Descending order\n")
myrev = mycol.find({} ,{"_id":0 ,"address":0}).sort("name" , -1)
for y in myrev:
    print(y)
