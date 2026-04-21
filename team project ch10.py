import pickle
import RetailItem
import CashRegister
def main(): #Tristan
    #main menu accpets no arguments
    #opens the retail store or inventory store
    print("--- Retail Store ---")
    print()
    print("Please choose from the options below:")
    print()
    print("To access the inventory control system, press 1.")
    print("To access the retail store, press 2.")
    print()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print()
        print("Welcome to the ACME system.")
        print()
        print("Inventory file doesn't exist, creating...")
        password = input("Enter the inventory control password: ")
        
        
    elif choice == 2:
        print("Opening Retail store...")
        Retail_Menu()
        
    else:
        print("Invalid choice.")
    
    while password != ("heisenberg"):
        print("Incorrect password, please try again.")
        password = input("Enter the inventory control password: ")
        
inventory_menu()
        
        
def inventory_menu(): #Bryson
    pass

def Retail_Menu(): #Tristan
    print("1 - View cart")
    print("2 - Display items for sale")
    print("3 - Purchase item")
    print("4 - Empty cart and start over")
    print("5 - Check out")
    print("6 - EXIT to main")
    option = int(input("Please enter a selection: "))
    keep_going = 'y'
    
    Retail1 = RetailItem.retailitem(description, units, price)
    
    if option == 1:
        print("Your cart is empty!")
    elif option == 3:
        print("Here is the current status of your inventory: ")

    