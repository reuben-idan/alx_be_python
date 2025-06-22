# oop/book_class.py

class Book:
    """
    A Book class that demonstrates Python magic methods.
    
    This class models a book with title, author, and publication year,
    and implements various magic methods for enhanced functionality.
    """
    
    def __init__(self, title, author, year):
        """
        Constructor (__init__) - Initializes a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor (__del__) - Called when the object is about to be destroyed.
        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String representation (__str__) - Returns a user-friendly string.
        
        Returns:
            str: A formatted string describing the book
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official representation (__repr__) - Returns a string that can recreate the object.
        
        Returns:
            str: A string representation that can be used to recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})" 