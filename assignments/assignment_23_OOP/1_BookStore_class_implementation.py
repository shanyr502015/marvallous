""" Write a Python program to implement a class named BookStore with the following specifications:
• The class should contain two instance variables:
        o Name (Book Name)
        o Author (Book Author)
• The class should contain one class variable:
        o NoOfBooks (initialize it to 0)
• Define a constructor (__init__) that accepts Name and Author and initializes instance variables.
• Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.
• Implement an instance method:
        o Display() : should display book details in the format: <BookName> by <Author>. No of books: <NoOfBooks>
Example usage:
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()   # Linux System Programming by Robert Love. No of books: 1
Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()   # C Programming by Dennis Ritchie. No of books: 2 """

class BookStore:
    NoOfBooks = 0
    
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1
    
    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")


# Example usage following the template pattern:
print("Class variable NoOfBooks:", BookStore.NoOfBooks)

obj1 = BookStore("Python Programming", "John Smith")
obj1.Display()
print("Instance variables:", obj1.Name, obj1.Author)

obj2 = BookStore("Data Science Handbook", "Jane Doe")
obj2.Display()
print("Instance variables:", obj2.Name, obj2.Author)

obj3 = BookStore("Machine Learning Basics", "Alice Johnson")
obj3.Display()
print("Instance variables:", obj3.Name, obj3.Author)
    
