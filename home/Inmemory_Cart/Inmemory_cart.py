class InMemoryCart:
    def __init__(self, cart_token,user_id,user_email):
        self.cart_token = cart_token
        self.user_id = user_id
        self.user_email = user_email
        
        self.items = {}  # Dictionary to hold items in the cart

    def add_item(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def get_items(self):
        return self.items
    def clear_cart(self):
        self.items = {}

    def get_cart_token(self):
        return self.cart_token

mycart = InMemoryCart("token123", "user1", "user1@example.com")
mycart2 = InMemoryCart("token456", "user2", "user2@example.com")

mycart.add_item("product1", 2)
mycart.add_item("product2", 1)  
mycart2.add_item("product3", 5)

print(mycart.get_items())  # Returns {'product1': 2, 'product2': 1}
print(mycart2.get_items())  # Returns {'product3': 5}

