import pandas as pd
import pickle
import warnings

def MakeBooksList():
    raw_books = pd.read_csv("books.csv")
    arr_of_books = []
    for index, row in raw_books.iterrows():
        book = Book(row["title"], row["book_id"], row["best_book_id"], row["authors"],
                    row["original_publication_year"],
                    row["isbn"], row["ratings_1"], row["ratings_2"], row["ratings_3"], row["ratings_4"],
                    row["ratings_5"],
                    row["image_url"], row["small_image_url"])
        arr_of_books.append(book)
    return arr_of_books

def MakeBookTitles():
    books = MakeBooksList()
    book_titles = []
    for book in books:
        book_titles.append(book.title)
    return book_titles

def Recommend(booknum, num_of_reccomendations):
    with open("book_model.pkl", 'rb') as file:
        model = pickle.load(file)
    with open("table.pkl", 'rb') as file:
        table = pickle.load(file)
    distance, suggestion = model.kneighbors(table.iloc[booknum, :].values.reshape(1, -1), n_neighbors=num_of_reccomendations + 1)
    return suggestion

def IDToBook(id, arr_of_books):
    for book in arr_of_books:
        if (book.id == id):
            return book
    return arr_of_books[0]

def BookToId(title, arr_of_books):
    for book in arr_of_books:
        if book.title == title:
            return book.id

class Book:
    def __init__(self, title, id, badid, author, year, isbn, one, two, three, four, five, url, smallUrl):
        self.title = title
        self.id = id
        self.badid = badid
        self.author = author
        self.year = year
        self.isbn = isbn
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.url = url
        self.smallUrl = smallUrl
