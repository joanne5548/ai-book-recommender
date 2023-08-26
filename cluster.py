import pandas as pd
import pickle

def MakeBooksList():
    raw_books = pd.read_csv("books.csv")
    arr_of_books = []
    for index, row in raw_books.iterrows():
        book = {"title": row["title"],
                "id": row["book_id"],
                "author": row["authors"],
                "year": row["original_publication_year"],
                "isbn": row["isbn"],
                "url": row["image_url"],
                "small_url": row["small_image_url"]}
        arr_of_books.append(book)
    return arr_of_books

def MakeBookTitles():
    books = MakeBooksList()
    book_titles = []
    for book in books:
        book_titles.append(book["title"])
    return book_titles

def Recommend(booknum, num_of_reccomendations):
    arr_of_books = MakeBooksList()
    with open("book_model.pkl", 'rb') as file:
        model = pickle.load(file)
    with open("table.pkl", 'rb') as file:
        table = pickle.load(file)
    distance, suggestion = model.kneighbors(table.iloc[booknum - 1, :].values.reshape(1, -1), n_neighbors=num_of_reccomendations+1)
    for i in range(len(suggestion[0])):
        suggestion[0][i] = suggestion[0][i] + 1
    books = []
    for j in range(1, len(suggestion[0])):
        books.append(IDToBook(suggestion[0][j], arr_of_books))
    return books

def IDToBook(id, arr_of_books):
    for book in arr_of_books:
        if (book["id"] == id):
            return book
    return arr_of_books[0]
