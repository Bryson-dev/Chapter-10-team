#class for cashregister
class CashRegister:
    def __init__(self):
        self.__cart = []

    def purchase_item(self, item):
        self.__cart.append(item)

    def get_total(self):
        total = 0.0
        for item in self.__cart:
            total += item.get_price_per_unit()
        return total

    def get_cart(self):
        if len(self.__cart) == 0:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.__cart:
                print(item)

    def empty(self):
        self.__cart = []

   
    def get_cart_items(self):
        return self.__cart

