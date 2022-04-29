
# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


class Library:
    def __init__(self,listofbooks,libraryname):
        self.listofbooks = listofbooks
        self.libraryname = libraryname
        self.dictionary = {}

    def display_books(self):
        print(f'Books Available in {self.libraryname} Library:')
        for i in self.listofbooks:
            print(i)

    def addbook(self,bookname):
        self.listofbooks.append(bookname)

    def lendbook(self,bookname,costumername):

        if bookname in self.listofbooks:
         self.dictionary.update({bookname : costumername})
         self.listofbooks.remove(bookname)
         print(f'Book Successfully lended to {costumername}')
        elif bookname in self.dictionary:
          print(f'The Book you want is with {self.dictionary[bookname]}')
        else :
            print('The book is not available in the library.')


    def returnbook(self,bookname,customername):
        if bookname in self.dictionary.keys() and customername.lower() == self.dictionary[bookname].lower():
            print(f'Book successfully returned by {customername}')
            del self.dictionary[bookname]
            self.listofbooks.append(bookname)
        else:
            print('Invalid input')


KavyaLibrary = Library(['Think Like a Monk','A Monk who sold his old ferrari','Gernimo Silton','HarryPotter-Part2','Maths-Ncert-class10'],'Crossword')
print('             Welcome To Library Management System    ')
while True:
    print('Type A to add book. ')
    print('Type R to return book. ')
    print('Type L to Lend book. ')
    print('Type D to display book. ')
    print('Type E to exit. ')
    textinput = input('Enter: ').lower()
    if textinput == 'a':
        book = input('\n Enter which book you want to add("only 1 book at a time"): ')
        KavyaLibrary.addbook(book)
        print('Your book is successfully added.\n')
        if input('Press any key to continue: ') : continue
    elif textinput == 'd':
        print('\n')
        KavyaLibrary.display_books()
        print('\n')
        if input('Press any key to continue: ') : continue
    elif textinput == 'l':
        print('\n')
        bookname = input('Enter the book\'s name: ')
        costumername = input('Enter the customer\'s name: ')
        KavyaLibrary.lendbook(bookname,costumername)
        if input('Press any key to continue: '): continue
    elif textinput == 'r':
        print('\n')
        bookname = input('Enter the book\'s name: ')
        costumername = input('Enter the customer\'s name: ')
        KavyaLibrary.returnbook(bookname,costumername)
        if input('Press any key to continue: '): continue
    elif textinput == 'e':
        print('Exited')
        break
    else:
        print('Invalid input')
        if input('Press any key to continue: '): continue
