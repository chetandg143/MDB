import pymongo
import csv
import  json
client = pymongo.MongoClient("mongodb://192.168.1.96/")
mydb = client['test']
mycol = mydb['emprecord']

# f1 = open("/home/tibil/Downloads/employees.csv" ,"r")
# data =csv.DictReader(f1)
# header = ["Empid","Name","Department" ,"Manager" ,"Salary"]
# for each in data:
#     row={}
#     for field in header:
#         row[field] =each[field]
#     mycol.insert(row)
# record = mycol.insert_many(data)

# x = mycol.find({},{"_id":0 ,"Empid":1,"Name":1 ,"Salary":1}).limit(5)
# for y in x:
#     print(y)

x = mycol.find({},{"_id":0})
for y in x:
    print(y)



# with open("emp.json", "w") as jsonFile:
#     jsonFile.write(json.dumps(y, indent = 4))
# #mycol.drop()