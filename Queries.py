#Queries


import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.1.96/")
mydb =myclient['test']
mycol = mydb['customers']

#myquery ={ "address":"White field"}
#myquery ={ "address": {"$gt": "S"}}
myquery ={ "address": {"$regex": "^W"}}




mydoc =mycol.find(myquery)




for x in mydoc:
    print(x)