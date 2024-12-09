class Author:  
    def __init__(self, name):  
        self.name = name  

    def __str__(self):  
        return self.name  


class Book:  
    def __init__(self, title, author):  
        self.title = title  
        self.author = author  # Author object must be associated when creating a Book  

    def display_info(self):  
        print(f"'{self.title}' is written by {self.author}.")  

    def __str__(self):  
        return f"Title: {self.title}, Author: {self.author}"  


# Example usage  
# Creating an Author instance  
author1 = Author("George Orwell")  
author2 = Author("Harper Lee")  

# Creating Book instances associated with Authors  
book1 = Book("1984", author1)  
book2 = Book("To Kill a Mockingbird", author2)  

# Displaying author and book information  
book1.display_info()  # Output: '1984' is written by George Orwell.  
book2.display_info()  # Output: 'To Kill a Mockingbird' is written by Harper Lee.  

# Displaying full information  
print(book1)  # Output: Title: 1984, Author: George Orwell  
print(book2)  # Output: Title: To Kill a Mockingbird, Author: Harper Lee