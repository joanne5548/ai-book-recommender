import pandas as pd
import numpy as np
from kmodes.kmodes import KModes
import matplotlib.pyplot as plt

def MakeBooksList():
    raw_books = pd.read_csv("books.csv")
    arr_of_books = []
    for index, row in raw_books.iterrows():
        book = Book(row["title"], row["book_id"] - 1, row["best_book_id"], row["authors"],
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

def MakeClusters():
    book_titles = MakeBookTitles()
    df = pd.read_csv("table.csv")
    print("read csv")
    df.pop(df.columns[0])
    df.columns = book_titles
    df.fillna('')
    df = df.astype(str)
    print(df)
    df.info()
    catColumnsPos = [df.columns.get_loc(col) for col in list(df.select_dtypes('object').columns)]
    print('Categorical columns           : {}'.format(list(df.select_dtypes('object').columns)))
    print('Categorical columns position  : {}'.format(catColumnsPos))
    dfMatrix = df.to_numpy()

    cost = []
    K = range(1, 100)
    for num_clusters in K:
        kmodes = KModes(n_clusters=num_clusters, init='random', n_init=5, verbose=1)
        kmodes.fit_predict(dfMatrix, categorical=catColumnsPos)
        cost.append(kmodes.cost_)

    plt.plot(K, cost, 'bx-')
    plt.title('Elbow')
    plt.xlabel('k-clusters')
    plt.ylabel('cost')
    plt.show()

def IDToBook(id, arr_of_books):
    for book in arr_of_books:
        if book.id == id:
            return book

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
