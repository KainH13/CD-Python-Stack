class Store:
    def __init__(self, name):
        self.name = name
        self.product_list = []


    def add_product(self, new_product):
        self.product_list.append(new_product)
        return self

    def sell_product(self, id):
        self.product_list.pop(id)
        self.product_list[id].print_info
        return self

    def inflation(self, percent_increase):
        for i in self.product_list:
            i.update_price(percent_increase, is_increased=True)
        return self

    def set_clearance(self, category, percent_discount):
        for i in self.product_list:
            if i.category == category:
                i.update_price(percent_discount, is_increased=False)
        return self

    def print_product_list(self):
        print("Printing Product Catalogue...")
        for i in self.product_list:
            i.print_info()
