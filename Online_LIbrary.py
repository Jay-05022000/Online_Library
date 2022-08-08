'''
------------------------------------Online Library(Based on OOP)-----------------------------------------------------------

user can do following things in library:
1) He/She can ask to provide a list of available books in library.
2) He/She can lend book of his/her choice from available books in library.If selected book is available then library will
  issue that book to user otherwise it will return the name of lender of that book.
3) User can donate books to library and it will record details of donations.
4) User can return lended books back to library and in this case library will update available books & Issued books.
5) It can give information about real time users and doners of library.'''


Issued_books=[]
Doners={}
Lended={}
lib_books=['p','q','r','s','t','u']

class library:
    def __init__(self,libname,availbooks):
        self.Lib_Name=libname
        self.Avil_Books=availbooks

    def Lend_Book(self,book_name,lender):
        if book_name in self.Avil_Books:
            print("you can avail this book")
            temp={book_name:lender}
            Lended.update(temp)
            lib_books.remove(book_name)
            Issued_books.append(book_name)
        else:
            Lended.get(book_name)
            print(f'Sorry,it is already lended by {Lended.get(book_name)}')

    def Add_Book(self,Doner_name,B_name):
        self.B_name=B_name
        self.Doner=Doner_name
        Doneted={Doner_name : B_name}
        Doners.update(Doneted)
        lib_books.append(self.B_name)
        print(f'Thanks {self.Doner} for your contribution,We have added this book to our library.')

    def Book_Return(self,u_name,b_name):
        self.name=u_name
        self.book=b_name
        print('Thanks for returning and making this book available for other users.')
        lib_books.append(b_name)

    def Lenders_info(self):
        print(f'These are our active users: {Lended}')

    def Doners_info(self):
        print(f'Meet our doners: {Doners}')


Jay_Lib=library("Jay",lib_books)
print(Jay_Lib.Avil_Books)
print('D:"Display books" \t L:"Lend book" \t A:"Add book" \t R:"Return book" \t Lend:"Lenders_info \t Don:"Doners_info \t Q:"Quit"')

while(True):
    User_Input=input('Hey User,welcome to our library What would you like to do?: ')
    try:
        if User_Input=='D':
            print(f'These books are currently available for use: {Jay_Lib.Avil_Books}')

        elif User_Input=='L':
            lender=input('Enter your name: ')
            Book_name=input("Enter name of book that you want: ")
            Jay_Lib.Lend_Book(Book_name,lender)

        elif User_Input=='A':
            print('Hey user,thank you for choosing to donate')
            Doner_name=input('Enter your name: ')
            B_name=input('Enter the name of book: ')
            Jay_Lib.Add_Book(Doner_name,B_name)

        elif User_Input=='R':
            u_name=input('Enter your name: ')
            b_name=input('Enter book name that you want to return: ')
            Jay_Lib.Book_Return(u_name,b_name)

        elif User_Input=="Lend":
            Jay_Lib.Lenders_info()

        elif User_Input=="Don":
            Jay_Lib.Doners_info()

        elif User_Input=="Q":
            break

        else:
            print('Choose appropriate option')
            continue

    except:
        print('Error occured due to inappropriate input')
        continue



