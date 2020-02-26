

import  pymongo

myclient  =pymongo.MongoClient("mongodb://192.168.1.96/")
mydb = myclient['test']
mycol = mydb['customers']

# myquery ={"address" :"Mountain 21"}
# mycol.delete_one(myquery)
# print("one record deleted")

# myquery = { "address": {"$regex": "^S"} }
#
# x = mycol.delete_many(myquery)
# print(x.deleted_count, " documents deleted.")


#Update Query
#
# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "White field" } }
#
# mycol.update_one(myquery, newvalues)
#
# #print "customers" after the update:
# for x in mycol.find():
#     print(x)

#limit statement


myquery = mycol.find().limit(5)
for x in myquery:
    print(x)