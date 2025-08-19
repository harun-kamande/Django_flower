class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, flower, quantity=1):
        self.items.append({'flower': flower, 'quantity': quantity})

    def remove_item(self, flower):
        self.items = [item for item in self.items if item['flower'] != flower]

    def get_total_price(self):
        return sum(item['flower'].price * item['quantity'] for item in self.items)
    
    def get_items(self):
        return self.items

    def clear(self):
        self.items = []
