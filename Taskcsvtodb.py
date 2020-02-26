

import pymongo
import csv
myclient = pymongo.MongoClient("mongodb://192.168.1.96/")
mydb = myclient['test']
coll = mydb['csvdata']

# file = open("Fire_Department_Calls.csv","r")
# reader =csv.DictReader(file)
# print("data Inserted ")
# data = coll.insert_many(reader)
#

q = coll.find({},{"Neighborhooods - Analysis Boundaries":1}).limit(10)
for x in q:
    print(x)