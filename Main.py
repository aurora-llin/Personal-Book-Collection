import storage

books = storage.load_books()
print(storage.update_book(books, 1, "Dune Messiah", "Frank Herbert", "Sci-Fi", "Finished"))  # True
print(storage.update_book(books, 99, "X", "X", "X", "X"))  # False
print(books)  # book 1 should show the new values