class Book():
    favourites = []
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
    def  is_long(self):
        if self.pages > 100:
            return True
        return False
    def __str__(self) :
        return f"{self.title} is {self.pages} pages long"
    def __eq__(self,other) :
        if self.title == other.title and self.pages == other.pages :
            return True
        return False
    def __hash__(self):
        return hash(self.title) ^ hash(self.pages)
book = Book("Agatha Christie",60)
book1 = Book("Agatha Christie",60)
Book.favourites.append(book)
Book.favourites.append(book1)
def do_something(book):
    book.title = "Something New"
do_something(book)
print(book)
open('input.txt' , 'a')
    
# print(book == book1)
# print(hash(book) == hash(book1))
