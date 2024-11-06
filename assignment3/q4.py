# Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total
# price.

class shoppingcart:
    def __init__(self):
        self.items=[]

    def addtocart(self,name,price,quantity=1):
        item= {'name': name,
              'price':price,
              'quantity': quantity
              }
        self.items.append(item)
        print(f"{quantity} {name} added to your cart of {price} each")

    def remove_item(self,name):
        for item in self.items:
            if item['name'] == name :
                self.items.remove(item)
                print(f'remove {name} from the cart')
            else:
                print(f'{name} not found in the cart')

    def total(self):
        sum=0
        for item in self.items:
            sum+= item['price']*item['quantity']
        return sum
    
    def showcart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.items:
                print(f"{item['name']} - Rs{item['price']} x {item['quantity']} = ", item['price']*item['quantity'])

cart = shoppingcart()
cart.addtocart('apple',150,5)
cart.addtocart('banana',60,12)
cart.showcart()
cart.remove_item('apple')
cart.showcart()
        
        
