

class Book: # create class шаблон кода, с пом котор созд объекты
    printed_class = "Printed"
    def __init__(self, name, author, color):  # kонструктор класса
        self.name = name #self это ссылка
        self.author = author
        self.color = color
    def pages(self):
        return "Has pages"
    def get_name(self):
        return f"Read my tytle {self.name}"

book1 = Book("Vianok", "Maksim Bahdanovich", "brown")
print(book1.name)
print(book1.get_name())
print(book1.color)
print(book1.printed_class)

book2 = Book("Spadchyna", "Yanka Kupala", "grey")
print(book2.printed_class)
print(book2.get_name())

class binding(Book):
   def __init__(self, name, author, color):
       super().__init__(name, author, color)

   def illustrations(self):
       return "Illustrations"

book_3 = binding(Book)("Stihi", "Yakub Kolas")
print(book3.get_name())
print(book3.printed_class)
print(book3.illustrations())