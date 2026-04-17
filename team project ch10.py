import pickle

def main(): #Tristan
    #This list will hold our objects
    inventory_list = []
    
    print("--- Retail Store ---")
    print()
    print("Please choose from the options below:")
    print()
    print("To access the inventory control system, press 1.")
    print("To access the retail store, press 2.")
    print()
    keep_going = 'y'
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print()
        print("Welcome to the ACME inventory control system.")
        print()
        print("Inventory file doesn't exist, creating...")
        password = input("Enter the inventory control password: ")
        
        
    elif choice == 2:
        print("Opening Retail store...")
        
    else:
        print("Invalid choice.")
        
def inventory_menu(): #Bryson
    pass

def Retail_Menu(): #Tristan
    pass