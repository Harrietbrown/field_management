import random
from wheat_class import *
from potato_class import *
from sheep_class import *
from cow_class import *

class Field(object):
    """Simulate a field that can contain animals and crops"""

    #constructor
    def __init__(self, max_animals,max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self,crop):
        if len(self._crops)<self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False
    def add_animal(self,animal):
        if len(self._animals)<self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False
    def harvest_crop(self,position):
        return self._crops.pop(position)
    def remove_animal(self,position):
        return self._animals.pop(position)
    def report_contents(self):
        crop_report=[]
        animal_report=[]
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        return {"crops":crop_report, "animals":animal_report}
    def report_needs(self):
        food = 0
        light = 0
        water = 0
        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"] > light:
                light = needs["light need"]
            if needs["water need"] > water:
                water = needs["water need"]
        for animal in self._animals:
            needs = animal.needs()
            food += needs["food need"]
            if needs["water need"]>water:
                water = needs["water need"]
        return{"food":food, "water":water, "light":light}
    def grow(self,light,food,water):
        #grow the crops
        if len(self._crops) >0:
            for crop in self._crops:
                crop.grow(light, water)
        if len(self._animals) >0:
            #all animals get same water
            #but total food must be shaired
            food_required = 0
            for animals in self._animals:
                needs = animals.needs()
                food_required += needs["food need"]
            #if we have more food than required work out how much each animal needs
            if food > food_required:
                additional_food = food - food_required
                food = food_required
            else:
                additional_food = 0
            #grow each animal
            for animal in self._animals:
                needs = animal.needs()
                if food >= needs["food need"]:
                    #remove the food needed for this animal from the total
                    food -= needs["food need"]
                    feed = needs["food need"]
                    #see if there is any additional food
                    if additional_food >0:
                        additional_food -= 1
                        #add this to the feed to be given to the animal
                        feed += 1
                else:
                    feed=food
                    food=0
                animal.grow(feed,water)

            
def auto_grow(field,days):
    for i in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        food = random.randint(1,100)
        field.grow(light,food,water)


def manual_grow(field):
    #get light, food and water values from user
    valid =False
    while valid == False:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1<= light <=10:
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
    valid = False
    while valid == False:
        try:
            food = int(input("Please enter a food value (1-100): "))
            if 1<=food<=100:
                valid = True
            else:
                print("Value entered is not valid.")
        except ValueError:
            print("Value entered is not valid.")
    field.grow(light,food,water)

def display_crops(crop_list):
    print()
    print("the following crops are in this field")
    pos =1
    for crop in crop_list:
        print("{0:>2}, {1}".format(pos,crop.report()))
        pos=pos + 1

def display_animals(animal_list):
    print()
    print("the following animals are in this field")
    pos =1
    for animal in animal_list:
        print("{0:>2}, {1}".format(pos,animal.report()))
        pos= pos + 1
        print(pos)

def select_crop(length_list):
    valid = False
    while not valid:
        try:
            selected = int(input("Please Select a Crop: "))
            if selected in range(0,length_list+1):
                valid = True
            else:
                print("please enter a valid option.")
        except ValueError:
            print("Please enter a valid option.")
    return selected -1

def select_animal(length_list):
    valid = False
    while not valid:
        try:
            selected = int(input("Please Select an animal: "))
            if selected in range(0,length_list+1):
                valid = True
            else:
                print("please select a valid option.")
        except ValueError:
            print("Please enter a valid option.")
    return selected -1

def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    if selected_crop == -1:
        return []
    else:
        return field.harvest_crop(selected_crop)

def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animal = select_animal(len(field._animals))
    if selected_animal == -1:
        return []
    else:
        return field.remove_animal(selected_animal)

def welcome_message():
    print("----------------------------------------------------------")
    print("             Welcome to crop farming simulator            ")
    print("----------------------------------------------------------")
    print("\n \n \n")

def display_crop_menu():
    print()
    print("Which crop type would you like to add?")
    print()
    print("1.   Wheat")
    print("2.   Potato")
    print()
    print("0.   I don't want to add a crop - Return me to the main menu")
    print("Please select an option")

def display_animal_menu():
    print()
    print("Which crop type would you like to add?")
    print()
    print("1.   Cow")
    print("2.   Sheep")
    print()
    print("0.   I don't want to add a crop - Return me to the main menu")
    print("Please select an option")

def display_main_menu():
    print()
    print("1.   Plant a new crop")
    print("2.   Harvest a crop")
    print()
    print("3.   Add a new animal")
    print("4.   Remove an animal")
    print()
    print("5.   Grow field Manually over one day")
    print("6.   Grow a field automatically over 30 days")
    print()
    print("7.   Report status of the field")
    print()
    print("0.   Exit the test program")
    print()
    print("Please select an option from the above menu")

def select_option(lower, upper):
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if lower <= choice <= upper:
                valid = True
            else:
                print("Please enter avalid option.")
        except ValueError:
            print("Please enter a valid option.")
    return choice

def plant_crop_to_field(field):
    display_crop_menu()
    choice = select_option(0,2)
    if choice == 1:
        if field.plant_crop(Wheat()):
            print()
            print("Wheat seeds planted")
        else:
            print("There is not enough space to plant any more wheat in this field")
    elif choice == 2:
        if field.plant_crop(Potato()):
            print()
            print("Potato seeds planted")
        else:
            print("There is not enough space to plant any more Potatos in this field")

def add_animal_to_field(field):
    display_animal_menu()
    choice = select_option(0,2)
    if choice == 1:
        name = input("What is this cow's name? ")
        if field.add_animal(Cow(name)):
            print()
            print("A baby cow Has been braught to the field")
        else:
            print("There is not enough space for any more cows in this field")
    elif choice == 2:
        name = input("What is this sheep's name?" )
        if field.add_animal(Sheep(name)):
            print()
            print("A baby sheep Has been braught to the field")
        else:
            print("There is not enough space for any more sheep in this field")

def manage_field(field):
    welcome_message()
    exit = False
    while not exit:
        display_main_menu()
        option = select_option(0,7)
        print()
        if option == 1:
            plant_crop_to_field(field)
        elif option == 2:
            removed_crop = harvest_crop_from_field(field)
            if removed_crop == []:
                pass
            else:
                print("You have removed the crop: {0}".format(removed_crop))
        elif option == 3:
            add_animal_to_field(field)
        elif option == 4:
            removed_animal = remove_animal_from_field(field)
            if removed_animal == []:
                pass
            else:
                print("You have removed the animal: {0}".format(removed_animal))
        elif option == 5:
            manual_grow(field)
        elif option == 6:
            auto_grow(field,30)
        elif option == 7:
            report = field.report_contents()
            print(report["animals"])
            print(report["crops"])
        elif option == 0:
            exit = True
            print()
    print("Thank you for joining us")


def main():
    new_field = Field(3,4)
    manage_field(new_field)


main()



