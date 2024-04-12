# Create a sub class SmartCoffeeMachine that inherits from KitchenAppliance.
# SmartCoffeeMachine have one more attribute: coffee_menu which is a default built-in menu of your choice which includes a list of coffee.
# SmartCoffeeMachine have two methods: update_menu and make_coffee.
# With update_menu method, users can add customised coffee names into the coffee_menu list. With make_coffee, coffee machine makes that type of coffee if it’s in the menu, otherwise, coffee machine will let the user know the item ordered doesn’t exist in the menu and print the menu to guide the user to pick something from the menu.


class KitchenAppliance:
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand
    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu
    def update_menu(self, new_coffee):
        pass
    def make_coffee(self, coffee_type):
        pass
my_coffee_machine = SmartCoffeeMachine(12334254, 'Ragdoll')
my_coffee_machine.report()
my_coffee_machine.update_menu('latte')
my_coffee_machine.update_menu('hazelnut latte')
my_coffee_machine.make_coffee('hazelnut latte')
my_coffee_machine.make_coffee('salted caramel latte') 

