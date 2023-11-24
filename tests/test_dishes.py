from lib.dishes import Dishes

def test_list_dishes_when_none_added():
        dishes_list = Dishes()
        assert dishes_list.list_dishes() == []

def test_add_one_dish_then_show_it():
        dishes_list = Dishes()
        dishes_list.add_dish("fish",1.0)
        assert dishes_list.list_dishes() == ["1, fish, £1.0"]


def test_add_five_dishs_then_show_it():
        dishes_list = Dishes()
        dishes_list.add_dish("fish",1.0)
        dishes_list.add_dish("cheesburgur",3.32)
        dishes_list.add_dish("bread loaf",0.25)
        dishes_list.add_dish("chips",1.9)
        dishes_list.add_dish("pie",3.65)
        assert dishes_list.list_dishes() == ["1, fish, £1.0", "2, cheesburgur, £3.32", "3, bread loaf, £0.25", "4, chips, £1.9", "5, pie, £3.65"]

def test_get_price_with_added_item():
        dishes_list = Dishes()
        dishes_list.add_dish("fish",1.0)
        dishes_list.add_dish("cheesburgur",3.32)
        dishes_list.add_dish("bread loaf",0.25)
        dishes_list.add_dish("chips",1.9)
        dishes_list.add_dish("pie",3.65)
        assert dishes_list.get_price("pie") == 3.65

def test_get_price_without_added_item():
        dishes_list = Dishes()
        dishes_list.add_dish("fish",1.0)
        dishes_list.add_dish("cheesburgur",3.32)
        dishes_list.add_dish("bread loaf",0.25)
        dishes_list.add_dish("chips",1.9)
        dishes_list.add_dish("pie",3.65)
        assert dishes_list.get_price("cake") == None

def test_is_dish_returns_false():
        dishes_list = Dishes()
        dishes_list.add_dish("fish",1.0)
        dishes_list.add_dish("cheesburgur",3.32)
        dishes_list.add_dish("bread loaf",0.25)
        dishes_list.add_dish("chips",1.9)
        dishes_list.add_dish("pie",3.65)
        assert dishes_list.is_dish("cake") == False

def test_is_dish_returns_true():
        dishes_list = Dishes()
        dishes_list.add_dish("fish",1.0)
        dishes_list.add_dish("cheesburgur",3.32)
        dishes_list.add_dish("bread loaf",0.25)
        dishes_list.add_dish("chips",1.9)
        dishes_list.add_dish("pie",3.65)
        assert dishes_list.is_dish("chips") == True