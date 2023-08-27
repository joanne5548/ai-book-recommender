import pymongo
import pickle
import json

def ReadPickleData():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    # mycol = mydb["model"]
    # with open("book_model.pkl", 'rb') as file:
    #     model = pickle.load(file)
    # x = mycol.insert_one(model)
    # print(x.inserted_id)
    with open("table.pkl", 'rb') as file:
        table = pickle.load(file)
    table.reset_index(inplace=True)
    table_dict = table.to_dict("records")
    anothercol = mydb["table"]
    print(type(table_dict))
    y = anothercol.insert_one(table_dict)
    print(y.inserted_id)