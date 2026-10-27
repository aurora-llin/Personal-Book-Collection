import json

DATA_FILE = "books.json"
VALID_STATUS = ["Not Started", "Reading", "Finished"]

def load_books():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=2)

def next_id(books):
    if not books:
        return 1
    return max((book["id"]) for book in books) + 1

def add_book(books, title, author, genre, status):
    book = {
        "id": next_id(books),
        "title": title,
        "author": author,
        "genre": genre,
        "status": status
    }
    books.append(book)
    save_books(books)
    return book

def find_by_id(books, book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

def update_book(books, book_id, title, author, genre, status):
    book = find_by_id(books, book_id)
    if book is None:
        return False
    book["title"] = title
    book["author"] = author
    book["genre"] = genre
    book["status"] = status
    save_books(books)
    return True