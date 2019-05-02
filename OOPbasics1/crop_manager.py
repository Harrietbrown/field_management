import random

class Crop(object):
    """A generic food crop"""

    #constructor
    def __init__(self,growth_rate, light_need, water_need):
        #set the attributes with an initial value

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "seed"
        self._type = "generic"
        #the above attributes are private and they should not be accessed directly from outside the class
    
    #return dictionary containing light and water needs
    def needs(self):
        return {"light need":self._light_need, "water need":self._water_need}
    #return a dictionary returning type status growth and days growing
    def report(self):
        return {"type":self._type, "status":self._status, "growth":self._growth, "days growing":self._days_growing}

    def _update_status(self):
        if self._growth >15:
            self._status = "old"
        elif self._growth >10:
            self._status = "mature"
        elif self._growth >5:
            self._status = "young"
        elif self._growth >0:
            self._status = "seedling"
        elif self._growth == 0:
            self._status = "seed"

    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            self._growth +=self._growth_rate
        #increment days growing
        self._days_growing += 1
        self._update_status()


def auto_grow(crop):
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
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def manual_grow(crop):
    #get light and water values from user
    valid =False
    while valid == False:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1<=light<=10:
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
    crop.grow(light,water)

def welcome_message():
    print("----------------------------------------------------------")
    print("             Welcome to crop farming simulator            ")
    print("----------------------------------------------------------")
    print("\n \n \n")

def display_menu():
    print("0:       Exit program")
    print("1:       Manualy grow crop")
    print("2:       Automaticaly grow crop")
    print("3:       Display crop report")
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


def manage_crop(crop):
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
            manual_grow(crop)
            print()
        elif choice == 2:
            auto_grow(crop)
            print()
        elif choice == 3:
            print(crop.report())
            print()
    print("thank you for using my program")


def main():
    welcome_message()
    manage_crop(new_crop)
