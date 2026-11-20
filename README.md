# Personal Book Collection

A command-line Python app to manage your books.

## Features
- Add, view, update, and delete books
- Search and filter by title, author, genre, or status
- Summary of your collection
- Data saved in books.json

## How to run
1. Install Python 3
2. Clone this repo
3. Run: python Main.py

## Files
- Main.py:  The menu and user interface. Shows the main menu, reads the
            user's input, displays books and summaries, and asks for confirmation before
            deleting. It hands all the real work to the BookManager and shows readable
            error messages instead of crashing.
- storage.py:   Loads and saves the book collection to a JSON file. A missing
                file is treated as an empty collection, and a damaged or unreadable file
                produces a clear error message instead of a crash.
- manager.py:   The `BookManager` class does the real work: it loads and
                saves books, adds, updates, and deletes them with unique IDs, searches and
                filters, and builds the summary. It uses `book.py` to validate input and
                `storage.py` to read and write the file.
- book.py:  Defines the `Book` class (id, title, author, genre, status) and
            validates book details, so empty fields or an invalid status are rejected
            with a clear message before anything is saved.

## Team
- Member 1: San Chhumphou (main.py)
- Member 2: Lin Thu Thu Tun (manager.py)
- Memeber 3: Phoung Yadane (book.py)
- Member 4: Ehav HOUR (storage.py)