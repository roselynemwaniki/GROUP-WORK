class Book:  
    def __init__(self, title, author):  
        self.title = title  
        self.author = author  
        self.is_borrowed = False  
        self.borrowed_by = None  # Will hold a reference to the Member who borrowed it  

    def lend(self, member):  
        if not self.is_borrowed:  
            self.is_borrowed = True  
            self.borrowed_by = member  
            return True  
        return False  

    def return_book(self):  
        if self.is_borrowed:  
            self.is_borrowed = False  
            self.borrowed_by = None  
            return True  
        return False  

    def __str__(self):  
        status = "Available" if not self.is_borrowed else f"Borrowed by {self.borrowed_by.name}"  
        return f"'{self.title}' by {self.author} - {status}"  


class Member:  
    def __init__(self, name):  
        self.name = name  
        self.borrowed_books = []  

    def borrow_book(self, book):  
        if len(self.borrowed_books) < 3:  
            if book.lend(self):  
                self.borrowed_books.append(book)  
                print(f"{self.name} borrowed '{book.title}'.")  
            else:  
                print(f"'{book.title}' is already borrowed.")  
        else:  
            print(f"{self.name} cannot borrow more than 3 books.")  

    def return_book(self, book):  
        if book in self.borrowed_books:  
            book.return_book()  
            self.borrowed_books.remove(book)  
            print(f"{self.name} returned '{book.title}'.")  
        else:  
            print(f"{self.name} does not have '{book.title}' borrowed.")  

    def borrowing_history(self):  
        return [book.title for book in self.borrowed_books]  

    def __str__(self):  
        return f"Member: {self.name}, Borrowed Books: {self.borrowing_history()}"  


class Library:  
    def __init__(self):  
        self.books = []  
        self.members = []  

    def add_book(self, book):  
        self.books.append(book)  

    def add_member(self, member):  
        self.members.append(member)  

    def display_available_books(self):  
        print("Available Books:")  
        for book in self.books:  
            print(book)  

    def check_member_history(self, member):  
        print(f"{member.name}'s Borrowing History: {member.borrowing_history()}")  


# Example usage  
library = Library()  

# Adding books to the library  
book1 = Book("1984", "George Orwell")  
book2 = Book("To Kill a Mockingbird", "Harper Lee")  
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")  
book4 = Book("Moby Dick", "Herman Melville")  

library.add_book(book1)  
library.add_book(book2)  
library.add_book(book3)  
library.add_book(book4)  

# Adding members to the library  
member1 = Member("Alice")  
member2 = Member("Bob")  

library.add_member(member1)  
library.add_member(member2)  

# Display available books  
library.display_available_books()  

# Borrowing books  
member1.borrow_book(book1)  # Alice borrows 1984  
member1.borrow_book(book2)  # Alice borrows To Kill a Mockingbird  
member1.borrow_book(book3)  # Alice borrows The Great Gatsby  
member1.borrow_book(book4)  # Alice cannot borrow Moby Dick (limit reached)  

# Checking member history  
library.check_member_history(member1)  

# Returning a book  
member1.return_book(book2)  # Alice returns To Kill a Mockingbird  

# Display available books again  
library.display_available_books()  

# Borrowing another book after returning one  
member1.borrow_book(book4)  # Alice borrows Moby Dick  
library.check_member_history(member1)