
class Books(object):
	
        def __init__(self,name,author):
		self.name = name
		self.author = author

	def get_book_details(self):
		return "The Name of the Book is %s and author is %s" %(self.name,self.author)

	def set_book_details(self,name,author):
		self.name = name
		self.author = author

book1 = Books("You Can Win", "Shiv Khera")
print book1.get_book_details()
book1.set_book_details("New Book", "Author yet not decided")
print book1.get_book_details()
