import pymongo
import pickle

def ReadPickleData():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    # mycol = mydb["model"]
    # with open("book_model.pkl", 'rb') as file:
    #     model = pickle.load(file)
    # x = mycol.insert_one(model)
    # print(x.inserted_id)
    with open("data/table.pkl", 'rb') as file:
        table = pickle.load(file)
    table.reset_index(inplace=True)
    dict = table.to_dict('records')
    print(dict)
    mydb.mycol.insert_many(dict)