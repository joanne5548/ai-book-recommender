import cluster

def main():
    suggestions = cluster.Recommend(29, 5)
    arr_of_books = cluster.MakeBooksList()
    print("Books like ", cluster.IDToBook(29, arr_of_books).title, ":")
    for i in range(0, len(suggestions)):
        print(suggestions[i].title, " by ", suggestions[i].author, " published in ", suggestions[i].year)
    print("")
    suggestions = cluster.Recommend(30, 5)
    arr_of_books = cluster.MakeBooksList()
    print("Books like ", cluster.IDToBook(30, arr_of_books).title, ":")
    for i in range(0, len(suggestions)):
        print(suggestions[i].title, " by ", suggestions[i].author, " published in ", suggestions[i].year)
    print("")
    suggestions = cluster.Recommend(48, 5)
    arr_of_books = cluster.MakeBooksList()
    print("Books like ", cluster.IDToBook(48, arr_of_books).title, ":")
    for i in range(0, len(suggestions)):
        print(suggestions[i].title, " by ", suggestions[i].author, " published in ", suggestions[i].year)

if __name__ == "__main__":
    main()
