#integrating mongodb


from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
myclient = pymongo.MongoClient("mongodb+srv://angela:<abcd>@cluster0-hmjop.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

mydb = myclient["locations"]
mycol = mydb["masseyHacks"]

containsLocation=true

while containsLocation = true:
    #insert code for choosing location
    
    name= "fill this in: variable of the string location chosen"
    mydestination = {name}
    if mydb.mycol.countDocuments({"name" : myDestination}, { limit: 1 }) == 1:
        containsLocation = true
    else:
        x = mycol.insert_one(mydestination)
        destinationid = x.inserted_id
        contains location = false:
        

#once the user is back home:
        mb.masseyHacks.delete_many({name: myDestination})
