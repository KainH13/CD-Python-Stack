class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * percent_change
        elif is_increased == False:
            self.price -= self.price * percent_change
        else:
            print("invalid value for 'is_increased' parameter, must be True or False")
        return self

    def print_info(self):
        print("_________Product Info:_________")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: {self.price}")
        return self