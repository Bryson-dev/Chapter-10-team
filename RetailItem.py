#Class
class RetailItem:
    def __init__(self, description, units, price):
        #Set up the data
        self.description = description
        self.units = units
        self.price = price

    #Getter methods
    def get_description(self):
        return self.description

    def get_units(self):
        return self.units

    def get_price(self):
        return self.price

    # This is what happens when we print the object
    def __str__(self):
        return "Description: " + self.description + \
               "\nUnits: " + str(self.units) + \
               "\nPrice: $" + str(self.price)