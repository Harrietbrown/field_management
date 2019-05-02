import random

class Animal(object):
    """A generic food animal"""

    #constructor
    def __init__(self,growth_rate, food_need, water_need, name):
        #set the attributes with an initial value

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "newborn"
        self._type = "generic"
        self._name = name
        #the above attributes are private and they should not be accessed directly from outside the class
    
    #return dictionary containing food and water needs
    def needs(self):
        return {"food need":self._food_need, "water need":self._water_need}
    #return a dictionary returning type status growth and days growing
    def report(self):
        return {"name":self._name, "type":self._type, "status":self._status, "Weight":self._growth, "days growing":self._days_growing}

    def _update_status(self):
        if self._growth >15:
            self._status = "old"
        elif self._growth >10:
            self._status = "adult"
        elif self._growth >5:
            self._status = "adolencant"
        elif self._growth >0:
            self._status = "baby"
        elif self._growth == 0:
            self._status = "newborn"

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._growth +=self._growth_rate
        #increment days growing
        self._days_growing += 1
        self._update_status()


def auto_grow(animal):
    #Get a number of days to autogrow
    valid = False
    while valid is False:
        try:
            days = int(input("How many days to autogrow? (enter 0 to return to main menu) "))
            if days >= 1:
                valid = True
            else:
                print("Value entered is not valid.")
        except ValueError:
            print("Value entered is not valid.")

    for i in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_grow(animal):
    #get food and water values from user
    valid =False
    while valid == False:
        try:
            food = int(input("Please enter a food value (1-10): "))
            if 1<= food <=10:
                valid = True
            else:
                print("Value entered is not valid.")
        except ValueError:
            print("Value entered is not valid")

    valid = False
    while valid == False:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1<=water<=10:
                valid = True
            else:
                print("Value entered is not valid.")
        except ValueError:
            print("Value entered is not valid.")
    animal.grow(food,water)

def welcome_message():
    print("----------------------------------------------------------")
    print("             Welcome to animal farming simulator            ")
    print("----------------------------------------------------------")
    print("\n \n \n")

def display_menu():
    print("0:       Exit program")
    print("1:       Manualy grow animal")
    print("2:       Automaticaly grow animal")
    print("3:       Display animal report")
    print("\n \n \n")
    print("please select option:")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option selected: "))
            if 0<= choice <= 3:
                option_valid = True
            else:
                print("Please enter avalid option.")
        except ValueError:
            print("Please enter a valid option.")
    return choice


def manage_animal(animal):
    print()
    noexit = True
    while noexit:
        display_menu()
        choice = get_menu_choice()
        print()
        if choice == 0:
            noexit = False
            print()
        elif choice == 1:
            manual_grow(animal)
            print()
        elif choice == 2:
            auto_grow(animal)
            print()
        elif choice == 3:
            print(animal.report())
            print()
    print("thank you for using my program")


def main():
    welcome_message()
    manage_animal(new_animal)
