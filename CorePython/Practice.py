class Store:
    def __init__(self, name, item):
        self.name = name
        self.item = []

    def add_item(self,name, price):
        item = {"name": name, "price": price}
        self.item.append(item)


    def stock_price(self):
        return sum([item["price"] for item in self.item])

    def __str__(self):
        print(f"")