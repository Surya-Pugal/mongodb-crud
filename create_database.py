import pymongo
import os
from dotenv import load_dotenv


load_dotenv()
mongo_uri = os.environ['MONGO_URI']
myclient=pymongo.MongoClient(mongo_uri)
mydb=myclient["SuryaTest"]
my_col=mydb["City"]

# mydict = {"city_id" : "L1P1W1", "address" : "Brownridge Place"}



# insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the inserted document.
def insert(city_name):

    last_id = my_col.find().sort([('city_id',-1)]).limit(1)
    try:
        last_id = last_id[0]['city_id']
    except:
        last_id = 0
    new_id = int(last_id) + 1

    

    new_row ={ 'city_id' : new_id, 'city_name':city_name}
    # print(new_row.inserted_id)
    my_col.insert_one(new_row)



# def update()

# x = my_col.find_one()
# print(x)

# for x in my_col.find():
#     print(x)

# for x in my_col.find({}, {"city_id" : 1}):
#     print(x)

# my_query = {"address" : "Williamsburg"}
# my_query = {"address" : {"$gt" : "S"}}
# my_query = {"address" : {"$regex" : "^D"}}

# my_doc = my_col.find(my_query)

# for x in my_doc:
#     print(x)

# my_doc = my_col.find().sort("city_id", -1)

# for x in my_doc:
#     print(x)

def startpy():
    insert("Oshawa")
    insert("Pickering")
    insert("Ajax")
    insert("Whitby")




























# from pymongo import MongoClient
# def get_database():
 
#    # Provide the mongodb atlas url to connect python to mongodb using pymongo
#    CONNECTION_STRING = "mongodb+srv://suryapugalenthi:nphBvsOUTICdQC45@suryatest.kkauduv.mongodb.net/test"
 
#    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#    client = MongoClient(CONNECTION_STRING)
 
#    # Create the database for our example (we will use the same database throughout the tutorial
#    return client['user_shopping_list']
  
# # This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":   
  
#    # Get the database
#    dbname = get_database()