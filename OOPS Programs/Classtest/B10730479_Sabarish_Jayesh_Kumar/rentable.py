from abc import ABC, abstractmethod                         # importing modules for using abstractclass

class RentableObject:                                       # Base Class Creation
    def __init__(self, name, available):                    # attrubuted definition
        self.name = name
        self.available = available
        self.rental_history = []

    def availability(self):                                 # making availability as default true
        self.available = "True"

    def show(self):                                         # method to check if objects are properly working
        print(f"{self.name} - {self.available}")
    
    @abstractmethod
    def rent_item(self, customer, days):                    # abstract class for rent_item as all other objects from other classes must adhere to
        self.customer = customer
        self.days = days
        self.available = "False"                            # making the availability to false
        self.rental_history.append({self.customer})         # Updating thr rental sheet
    
    def return_item(self, returning_customer_name):         
        self.returning_customer_name = returning_customer_name
        self.available = "True"                             # making the availablity as True again after returning
        print(f"Thank you for returning, Return Successfull")
    
class Book(RentableObject):                                 # creating a subclass book from parent class Rentable object
    def __init__(self, name, available, author):
        super().__init__(name, available)                   # inherting attributes from parent class
        self.author = author
    
    def show(self):
        super().show()                                      # inheriting functionalities from parent class
        print(f"{self.author}")

    def rent_item(self, customer, days):
        super().rent_item(customer, days)
        print(f"please note the maximum time for renting book is 14 days")   # notifying customer maximum duration is 14 days
    
    def return_item(self, returning_customer_name):
        super().return_item(returning_customer_name)
        print(f"item returned is {self.name}")


class DVD(RentableObject):
    def __init__(self, name, available, director):
        super().__init__(name, available)
        self.director = director
    
    def show(self):
        super().show()
        print(f"{self.director}")

    def rent_item(self, customer, days):
        super().rent_item(customer, days)
        print(f"please note maximum time allowed for renting DVD is 7 days")   # notifuing customer about maximum days is 7
    
    def return_item(self, returning_customer_name):
        super().return_item(returning_customer_name)
        print(f"the item returned is {self.name}")
    
    # Creating required objects to test classes  #

RentableObject_laptop = RentableObject("acer_laptop", "True")
RentableObject_laptop.show()
Book_harrypotter = Book("harry_potter", "True", "JK Rowling")
Book_harrypotter.show()
DVD_Dark_knight = DVD("Dark_Knight", "True", "Christopher_Nolan")
DVD_Dark_knight.show()

# additional functionalities for showing, renting & returning #

def show_items_available():
    print("-------------------------------------")
    print(f"these are the availble item to rent")
    print("--------------------------------------")

    for i in (RentableObject_laptop, Book_harrypotter, DVD_Dark_knight):   # Polymorphism Usage to iterate through objects & classes using same a same function name
        i.show()

def rent_harry_potter():
    Book_harrypotter.rent_item("Mr.Xyz", "14")

def return_harry_potter():
    Book_harrypotter.return_item("Mr.XYZ")

#function for displaying the rental sheet of an object #

def show_rental_harry_potter():
 print(Book_harrypotter.rental_history)


show_items_available()
rent_harry_potter()
show_items_available()
return_harry_potter()
show_items_available()
show_rental_harry_potter()











        