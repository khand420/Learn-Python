

class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}


# Display the book 
    def displayBooks(self):
        print(f"We have Books in our Library: {self.name}")
        for book in self.bookList:
            print(book)


# Lend the book 
    def lendBooks(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book Database has been Updated. You can take your book now!")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")


# Add book 
    def addBooks(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list")


    def returnBooks(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    obj = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basic', 'Algorithm by CLRS'], "CODE2HELL")

    while(True):
        print(f"Welcome to the {obj.name} libary. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend Books") 
        print("3. Add Books") 
        print("4. Return Books") 


        user_choice = input()
        if user_choice not in ['1', '2', '3', '4',]:
            print("Please Enter valid Option!\n")
            continue
        else:
            user_choice = int(user_choice)  



        if user_choice == 1:
            obj.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to Lend: ")
            user = input("Enter you Name: ")
            obj.lendBooks(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to Add:")       
            obj.addBooks(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to Return:")       
            obj.returnBooks(book)  

        else:
            print("Not a valid Option!") 



        # For quit or continue the libary 
        print("Press q to Quit and c Continue")
        user_choice2 = ""
        while(user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue         



