class Dishes():
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish, price):
        self.dishes.append({"dish":dish, "price":price})

    def list_dishes(self):
        if self.dishes == []:
            return self.dishes
        list2 = []
        counter = 1
        for item in self.dishes:
            item_text = item["dish"]
            price_text = item["price"]
            text = f"{counter}, {item_text}, £{price_text}"
            #text = f"{counter}, {item["dish"]}, £{item["price"]}"
            list2.append(text)
            counter += 1
        return list2

    def get_price(self, dish):
        for item in self.dishes:
            if item["dish"] == dish:
                return item["price"]
            
    def is_dish(self, dish):
        for item in self.dishes:
            if item["dish"] == dish:
                return True
        return False