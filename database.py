import pymongo
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
myclient = pymongo.MongoClient("mongodb+srv://angela:<abcd>@cluster0-hmjop.azure.mongodb.net/test?retryWrites=true&w=majority")
db = myclient.test

mydb = myclient["locations"]
mycol = mydb["masseyHacks"]

def insert(location):
    mycol.insert_one({"name":location})

def check(location):
    if mydb.mycol.countDocuments({"name" : location}) > 0:
        return True
    else:
        return False

