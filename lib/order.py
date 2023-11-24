class Order():
    def __init__(self, dishes):
        self.dishes = dishes
        self.orderes = []

    def order_item(self, dish, quantity):
        if self.dishes.is_dish(dish):
            self.orderes.append(dish)
            self.orderes.append(quantity)
            
    def show_recite(self):
        total = 0
        text = ""
        for item in range(0, len(self.orderes), 2):
            price = self.dishes.get_price(self.orderes[item]) * self.orderes[item+1]
            total += price
            text += self.orderes[item] + " " + str(self.orderes[item+1]) + " £" + str(price) + ", "
        text += "total £" + str(total)
        return text