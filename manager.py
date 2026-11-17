import storage
from book import Book, VALID_STATUS, check_text, validate_book


class BookNotFound(Exception):
    """No book has the requested ID."""


class BookManager:
    def __init__(self, data_file):
        self.data_file = data_file
        # A dictionary keyed by ID: finding, updating or deleting a book by
        # its ID is a direct lookup, and the same ID cannot be stored twice.
        self.books = {}

    # ----- loading and saving -----

    def load(self):
        """Load saved books. Returns a message to show, or None if all is fine."""
        try:
            records = storage.load_records(self.data_file)
            loaded = {}
            for record in records:
                book = self.record_to_book(record)
                if book.id in loaded:
                    raise storage.DataFileError("an ID appears twice")
                loaded[book.id] = book
            self.books = loaded
            return None
        except storage.DataFileError as error:
            backup = storage.preserve_damaged_file(self.data_file)
            self.books = {}
            return ("Your data file is damaged (" + str(error) + ").\n"
                    "The original was kept as '" + backup + "'.\n"
                    "Starting with an empty library.")

    def record_to_book(self, record):
        """Turn one saved record into a Book, or raise DataFileError."""
        if not isinstance(record, dict):
            raise storage.DataFileError("a record is not an object")
        book_id = record.get("id")
        if not isinstance(book_id, int) or book_id < 1:
            raise storage.DataFileError("a record has a bad ID")
        try:
            title, author, genre, status = validate_book(
                record.get("title"), record.get("author"),
                record.get("genre"), record.get("status"))
        except ValueError as error:
            raise storage.DataFileError("a record is invalid: " + str(error))
        return Book(book_id, title, author, genre, status)

    def save(self):
        records = [book.to_dict() for book in self.all_books()]
        storage.save_records(self.data_file, records)

    # ----- add, get, update, delete -----

    def next_id(self):
        if len(self.books) == 0:
            return 1
        return max(self.books) + 1

    def add_book(self, title, author, genre, status):
        title, author, genre, status = validate_book(title, author, genre, status)
        book = Book(self.next_id(), title, author, genre, status)
        self.books[book.id] = book
        self.save()
        return book

    def get_book(self, book_id):
        """Find a book by ID. Accepts text such as "3" or the number 3."""
        try:
            book_id = int(book_id)
        except (TypeError, ValueError):
            raise ValueError("ID must be a whole number.")
        if book_id not in self.books:
            raise BookNotFound("No book with ID " + str(book_id) + ".")
        return self.books[book_id]

    def update_book(self, book_id, title, author, genre, status):
        """Change a book. Empty values keep the current information."""
        book = self.get_book(book_id)
        title, author, genre, status = validate_book(
            title or book.title, author or book.author,
            genre or book.genre, status or book.status)
        book.title = title
        book.author = author
        book.genre = genre
        book.status = status
        self.save()
        return book

    def delete_book(self, book_id):
        book = self.get_book(book_id)
        del self.books[book.id]
        self.save()

    # ----- viewing, searching, summary -----

    def all_books(self):
        return sorted(self.books.values(), key=lambda book: book.id)

    def search(self, keyword):
        keyword = check_text(keyword, "Keyword").lower()
        found = []
        for book in self.all_books():
            if keyword in book.title.lower() or keyword in book.author.lower():
                found.append(book)
        return found

    def filter_by_status(self, status):
        status = validate_book("x", "x", "x", status)[3]
        return [book for book in self.all_books() if book.status == status]

    def summary(self):
        by_status = {}
        for status in VALID_STATUS:
            by_status[status] = 0
        by_genre = {}
        for book in self.books.values():
            by_status[book.status] += 1
            by_genre[book.genre] = by_genre.get(book.genre, 0) + 1
        total = len(self.books)
        completion = 0
        if total > 0:
            completion = by_status["Finished"] / total * 100
        return {"total": total, "by_status": by_status,
                "by_genre": by_genre, "completion": completion}