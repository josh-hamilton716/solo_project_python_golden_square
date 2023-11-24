from lib.dishes import Dishes
from lib.order import Order

def test_order_an_item():
    dishes_list = Dishes()
    dishes_list.add_dish("fish",1.0)
    dishes_list.add_dish("cheesburgur",3.32)
    dishes_list.add_dish("bread loaf",0.25)
    dishes_list.add_dish("chips",1.9)
    dishes_list.add_dish("pie",3.65)
    order1 = Order(dishes_list)
    order1.order_item("fish",1)
    assert order1.orderes == ["fish", 1]

def test_show_recite_after_one_item_ordered():
    dishes_list = Dishes()
    dishes_list.add_dish("fish",1.0)
    dishes_list.add_dish("cheesburgur",3.32)
    dishes_list.add_dish("bread loaf",0.25)
    dishes_list.add_dish("chips",1.9)
    dishes_list.add_dish("pie",3.65)
    order1 = Order(dishes_list)
    order1.order_item("fish",1)
    assert order1.show_recite() == "fish 1 £1.0, total £1.0"

def test_show_recite_after_two_item_ordered():
    dishes_list = Dishes()
    dishes_list.add_dish("fish",1.0)
    dishes_list.add_dish("cheesburgur",3.32)
    dishes_list.add_dish("bread loaf",0.25)
    dishes_list.add_dish("chips",1.9)
    dishes_list.add_dish("pie",3.65)
    order1 = Order(dishes_list)
    order1.order_item("fish",1)
    order1.order_item("cheesburgur",1)
    assert order1.show_recite() == "fish 1 £1.0, cheesburgur 1 £3.32, total £4.32"

def test_show_recite_after_big_order():
    dishes_list = Dishes()
    dishes_list.add_dish("fish",1.0)
    dishes_list.add_dish("cheesburgur",3.32)
    dishes_list.add_dish("bread loaf",0.25)
    dishes_list.add_dish("chips",1.9)
    dishes_list.add_dish("pie",3.65)
    order1 = Order(dishes_list)
    order1.order_item("fish",2)
    order1.order_item("cheesburgur",2)
    order1.order_item("chips",4)
    order1.order_item("bread loaf",3)
    order1.order_item("pie",1)
    assert order1.show_recite() == "fish 2 £2.0, cheesburgur 2 £6.64, chips 4 £7.6, bread loaf 3 £0.75, pie 1 £3.65, total £20.64"

def test_show_recite_after_two_item_ordered_and_one_not_on_menue():
    dishes_list = Dishes()
    dishes_list.add_dish("fish",1.0)
    dishes_list.add_dish("cheesburgur",3.32)
    dishes_list.add_dish("bread loaf",0.25)
    dishes_list.add_dish("chips",1.9)
    dishes_list.add_dish("pie",3.65)
    order1 = Order(dishes_list)
    order1.order_item("fish",1)
    order1.order_item("cheesburgur",1)
    order1.order_item("cake",1)
    assert order1.show_recite() == "fish 1 £1.0, cheesburgur 1 £3.32, total £4.32"