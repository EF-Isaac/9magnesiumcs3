class Publication:
  def func1(self):
    print("the author and title of the work is:.")

class Book(Publication):
  def func2(self):
    print("number of pages in the book:.")

class Magazine(Publication):
  def func3(self):
    print("issue number:.")

obj = Book()
obj.func1()
obj.func2()
