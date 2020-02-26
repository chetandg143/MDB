import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.1.96/")
mydb = myclient['test']
mycol = mydb['test1']
print("data inserted  to mongodb")
mydict ={"name":"Chetan" , "mname":"D" , "Lname":"Goudar"}

x =mycol.insert_one(mydict)

