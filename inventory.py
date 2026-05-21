class Inventory:
    def __init__(self, initial_items=None):
        self.items = initial_items or {}

    def add_item(self, name, quantity):
        self.items[name] = quantity

    def get_stock(self, name):
        return self.items.get(name, 0)

    def check_low_stock(self, threshold=10):
        return [name for name, qty in self.items.items() if qty < threshold]
