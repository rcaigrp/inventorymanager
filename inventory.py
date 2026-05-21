class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, quantity, price):
        self.items[item_id] = {'name': name, 'quantity': quantity, 'price': price}

    def remove_item(self, item_id):
        self.items.pop(item_id, None)

    def get_item(self, item_id):
        return self.items.get(item_id)

    def get_total_value(self):
        total = 0
        for item in self.items.values():
            total += item['quantity'] * item['price']
        return total

    def get_low_stock_items(self, threshold=5):
        return [item for item in self.items.values() if item['quantity'] < threshold]


def add_item(inventory, item_id, name, quantity, price):
    inventory.add_item(item_id, name, quantity, price)


def remove_item(inventory, item_id):
    inventory.remove_item(item_id)


def get_item(inventory, item_id):
    return inventory.get_item(item_id)


def get_total_value(inventory):
    return inventory.get_total_value()


def get_low_stock_items(inventory, threshold=5):
    return inventory.get_low_stock_items(threshold)
