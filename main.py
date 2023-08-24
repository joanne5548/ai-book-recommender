import cluster

def main():
    suggestions = cluster.Recommend(1, 6)
    arr_of_books = cluster.MakeBooksList()
    print("Books like ", cluster.IDToBook(suggestions[0][0], arr_of_books).title, ":")
    for i in range(1, len(suggestions[0])):
        print(cluster.IDToBook(suggestions[0][i], arr_of_books).title, "by ", cluster.IDToBook(suggestions[0][i], arr_of_books).author)

    print(" ")

    suggestions = cluster.Recommend(2, 6)
    print("Books like ", cluster.IDToBook(suggestions[0][0], arr_of_books).title, ":")
    for i in range(1, len(suggestions[0])):
        print(cluster.IDToBook(suggestions[0][i], arr_of_books).title, "by ", cluster.IDToBook(suggestions[0][i], arr_of_books).author)
    print(" ")

    suggestions = cluster.Recommend(3, 6)
    print("Books like ", cluster.IDToBook(suggestions[0][0], arr_of_books).title, ":")
    for i in range(1, len(suggestions[0])):
        print(cluster.IDToBook(suggestions[0][i], arr_of_books).title, "by ", cluster.IDToBook(suggestions[0][i], arr_of_books).author)

if __name__ == "__main__":
    main()
