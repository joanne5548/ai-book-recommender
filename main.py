import backend.book
import database


def main():
    database.ReadPickleData()
    backend.book.app.run()

if __name__ == "__main__":
    main()