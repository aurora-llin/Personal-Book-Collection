# Personal Book Collection

A command-line Python app for keeping track of the books you own and your reading progress. Your collection is saved to a JSON file, so it is still there the next time you open the program.

## Features

- Add a book with a title, author, genre, and reading status. Each book gets a unique ID automatically, and empty fields or invalid statuses are rejected.
- View all books in a table, with a friendly message when the collection is empty.
- Search by title or author (partial matches work, and case is ignored).
- Filter by reading status (Not Started, Reading, or Finished).
- Update a book by its ID. Press Enter to keep a field unchanged.
- Delete a book by its ID, with a yes/no confirmation first.
- Summary showing the total number of books, the count for each status, the completion rate, and the number of books per genre.
- Automatic saving to books.json after every successful change, so closing the program never loses completed work.
Safe error handling: invalid input, unknown IDs, and a missing data file do not crash the program.

## How to run

Requirements: Python 3.8 or newer. No extra packages are needed.

1. Check that Python is installed:

python --version

2. Clone this repository (or download and unzip it), then open a terminal in the project folder:

git clone <your-repository-url>
cd <project-folder>

3. Run the program from inside that folder:

python main.py

## Files

Personal-Book_Collection/

├── main.py       # Menu and user interface
├── manager.py    # BookManager class: the program logic
├── book.py       # Book class and validation rules
├── storage.py    # Reading and writing the JSON file
└── books.json    # Saved books (created automatically)

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

How they connect: main.py → manager.py → book.py and storage.py. Each file only uses the files to its right, never the other way around.

## Known Limitations

- Single user, one file: The program is designed for one person on one computer. There is no login, and two copies running at once could overwrite each other's changes.
- Run from the project folder: The data file path is relative, so books.json is created in whatever folder you run the program from.
- Limited search: Search covers title and author only. Filtering covers status only (there is no genre filter), and the list is always sorted by ID.
- Typed input: Statuses must be typed out (case does not matter). One invalid entry returns you to the main menu, so you retype that action from the start.
- IDs can be reused: If you delete the book with the highest ID, the next new book takes that ID again. IDs are always unique at any one time.
- No duplicate check: You can add two books with the same title and author.
- Saving can fail: If the file cannot be written (for example, a read-only folder), an error is shown and that change will not be on disk, even though it appears in the current session.
- Empty file counts as damaged: A completely empty books.json is not valid JSON, so it is renamed aside and the program starts fresh.
- Manual testing only: The program was tested by hand using the testing table, not with automated tests.

## Team

- Member 1: San Chhumphou (main.py)
- Member 2: Lin Thu Thu Tun (manager.py)
- Memeber 3: Phoung Yadane (book.py)
- Member 4: Ehav HOUR (storage.py)