import storage
from book import VALID_STATUS
from manager import BookManager, BookNotFound

DATA_FILE = "books.json"
STATUS_TEXT = "/".join(VALID_STATUS)


def show_books(books, empty_message):
    if len(books) == 0:
        print("\n" + empty_message)
        return
    print("\nID   Title                          Author               Genre                Status")
    print("-" * 85)
    for b in books:
        print(f"{b.id:<4} {b.title[:29]:<30} {b.author[:19]:<20} {b.genre[:19]:<20} {b.status}")


def add_book(manager):
    print("\n--- Add a Book ---")
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    status = input("Status (" + STATUS_TEXT + "): ")
    book = manager.add_book(title, author, genre, status)
    print("Added '" + book.title + "' with ID " + str(book.id) + ".")


def view_books(manager):
    show_books(manager.all_books(), "Your library is empty. Add a book to get started!")


def search_books(manager):
    print("\n1. Search by title or author")
    print("2. Filter by status")
    choice = input("Choose: ").strip()
    if choice == "1":
        keyword = input("Keyword: ")
        show_books(manager.search(keyword), "No books match '" + keyword + "'.")
    elif choice == "2":
        status = input("Status (" + STATUS_TEXT + "): ")
        show_books(manager.filter_by_status(status), "No books with that status.")
    else:
        print("Invalid choice.")


def update_book(manager):
    print("\n--- Update a Book ---")
    book = manager.get_book(input("Book ID: "))
    print("Press Enter to keep the current value.")
    title = input("Title [" + book.title + "]: ").strip()
    author = input("Author [" + book.author + "]: ").strip()
    genre = input("Genre [" + book.genre + "]: ").strip()
    status = input("Status [" + book.status + "]: ").strip()
    manager.update_book(book.id, title, author, genre, status)
    print("Book updated.")


def delete_book(manager):
    print("\n--- Delete a Book ---")
    book = manager.get_book(input("Book ID: "))
    answer = input("Delete '" + book.title + "' by " + book.author + "? (y/n): ")
    if answer.strip().lower() == "y":
        manager.delete_book(book.id)
        print("Book deleted.")
    else:
        print("Deletion cancelled.")


def show_summary(manager):
    info = manager.summary()
    print("\n--- Library Summary ---")
    print("Total books:", info["total"])
    if info["total"] == 0:
        print("Add some books to see more stats.")
        return
    for status, count in info["by_status"].items():
        print("  " + status + ":", count)
    print("Completion rate: " + str(round(info["completion"])) + "%")
    print("Books per genre:")
    for genre, count in sorted(info["by_genre"].items()):
        print("  " + genre + ":", count)


def run_menu(manager):
    while True:
        print("\n=== Book Tracker ===")
        print("1. Add book")
        print("2. View all books")
        print("3. Search / filter")
        print("4. Update book")
        print("5. Delete book")
        print("6. Summary")
        print("7. Quit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                add_book(manager)
            elif choice == "2":
                view_books(manager)
            elif choice == "3":
                search_books(manager)
            elif choice == "4":
                update_book(manager)
            elif choice == "5":
                delete_book(manager)
            elif choice == "6":
                show_summary(manager)
            elif choice == "7":
                print("Goodbye!")
                return
            else:
                print("Invalid option, try again.")
        except (ValueError, BookNotFound, storage.StorageError) as error:
            print("Error:", error)


def main():
    manager = BookManager(DATA_FILE)
    try:
        message = manager.load()
    except storage.StorageError as error:
        print("Cannot start:", error)
        return
    if message:
        print("\n" + message)
    try:
        run_menu(manager)
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye! (Completed changes were already saved.)")


if __name__ == "__main__":
    main()