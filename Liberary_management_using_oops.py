
class Library:
    info = {}
    def __init__(self,book_list,library_name):
        self.book_list=book_list
        self.library_name=library_name

    def lend_book(self):
        self.username_lended=input('enter your name:')
        self.book_lended=input('please enter the book name to be lended: ')

        if self.book_lended in self.book_list:
            self.info.update({self.book_lended: self.username_lended})
            self.book_list.remove(self.book_lended)
        else:
            print('---NO SUCH BOOK IS AVAIABLE---  ')

    def display_book(self):
        print('---BOOKS AVAIABLE ARE---')
        for i in self.book_list:
            print(i)
        if self.info:
            print('---Lended Books Are ---')
            print(self.info)

    def add_book(self):
        self.donate_book=input('Enter The Book Name:')
        self.book_list.append(self.donate_book)
        print('---Thank You For Donating Your Book---')

    def return_book(self):
        self.returned_book=input('Enter The Name Of To Be Returned:')
        if self.returned_book in self.info.keys():
            del(self.info[self.returned_book])
            print('---Hope You Enjoy This Book---')
        else:
            print('---No Such Book Lended Please Check Your Book Name---')

lib_name=input('Enter Your Library Name:')
lib_books=input('Enter your Library Books Name Seprate By Comma(,)--').split(',')
obj=Library(lib_books,lib_name)
while True:
    cho=input('''
        Press 1:for Display All Book In Your Library, 
        Press 2:for Lending Book,
        Press 3:for Donating Book In  Library, 
        Press 4:for Return The Library  Book---:''')


    if cho=='1':
        obj.display_book()
    elif cho=='2':
        obj.lend_book()
    elif cho=='3':
        obj.add_book()
    elif cho=='4':
        obj.return_book()
    else:
        print('Nothing To Done')