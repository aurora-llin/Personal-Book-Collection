VALID_STATUS = ["Not Started", "Reading", "Finished"]


def check_text(value, name):
    #This one is for checking and making sure the value is a string and not empty
    if not isinstance(value, str) or value.strip() == "":
        raise ValueError(name + " is required.")
    return value.strip()


def validate_book(title, author, genre, status):
    #This function validates the book information and returns the validated values.
    title = check_text(title, "Title")
    author = check_text(author, "Author")
    genre = check_text(genre, "Genre")
    status = check_text(status, "Status")
    #This one is for checking and making sure the status is one of the valid statuses
    for valid in VALID_STATUS:
        if status.lower() == valid.lower():
            return title, author, genre, valid
    raise ValueError("Status must be one of: " + ", ".join(VALID_STATUS))


class Book:
    def __init__(self, book_id, title, author, genre, status):
        self.id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "status": self.status,
        }