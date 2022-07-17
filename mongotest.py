import pymongo

client = pymongo.MongoClient("mongodb+srv://mrunalsawant:mongodb123.v2anxnk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

Hello all....