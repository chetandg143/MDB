
import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.1.96/")
mydb =myclient['test']
mycol = mydb['customers']
print("data inserted! ")
# mylist =[
#     { "name": "Amar" ,"address": "White field"},
#     { "name": "Amy", "address": "Apple st 652"},
#     { "name": "Hannah", "address": "Mountain 21"},
#     { "name": "Michael", "address": "Valley 345"},
#     { "name": "Sandy", "address": "Ocean blvd 2"},
#     { "name": "Betty", "address": "Green Grass 1"},
#     { "name": "Richard", "address": "Sky st 331"},
#     { "name": "Susan", "address": "One way 98"},
#     { "name": "Vicky", "address": "Yellow Garden 2"},
#     { "name": "Ben", "address": "Park Lane 38"},
#     { "name": "William", "address": "Central st 954"},
#     { "name": "Chuck", "address": "Main Road 989"},
#     { "name": "Viola", "address": "Sideway 1633"}
# ]

#print only name and address
# for x in mycol.find({},{ "_id":0, "name":1 , "address":1}):
#     print(x)

#print only names
for x in mycol.find({} ,{"_id":0 ,"address":0}):
    print(x)