Multi-Class Planned Design Recipe
1. Describe the Problem
Typically you will be given a short statement that does this called a user story. In industry, you may also need to ask further questions to clarify aspects of the problem.

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.


dishes class
list of dishes
list of dishes contains dish and price
show list of dishes with itemized number for each

order_class
order a dish with number for quanity of dish
show recite

2. Design the Class System
Design the interfaces of each of your classes and how they will work together to achieve the job of the program. You can use diagrams to visualise the relationships between classes.

Consider pulling out the key verbs and nouns in the problem description to help you figure out which classes and methods to have.

class Dishes()
    def __init__(self):
        pass

    def add_dish(self, dish, price):
        pass

    def list_dishes(self):
        pass

    def get_price(self, dish):
        pass

class Order()
    def __init__(self, dishes):
        pass

    def oder_item(self, dish, quantity):
        pass

    def show_recite(self):
        pass


Steps 3, 4, and 5 then operate as a cycle.

3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

Encode one of these as a test and move to step 4.

4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

Encode one of these as a test and move to step 5.

5. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the class to behave according to your example.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.