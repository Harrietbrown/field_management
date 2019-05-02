from field_class import *

def display_menu_crop():
    print("what sort of crop would you like to plant?")
    print()
    print("    1:   Wheat ")
    print("    2:   Potato")
    print()

def display_menu_animal():
    print("what sort of animal would you like to raise?")
    print()
    print("    1:   Cow  ")
    print("    2:   Sheep")
    print()

def select_option(options):
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option selected: "))
            if choice in options:
                option_valid = True
            else:
                print("Please enter avalid option.")
        except ValueError:
            print("Please enter a valid option.")
    return choice

def create_crop():
    display_menu_crop()
    choice = select_option([1,2])
    if choice == 1:
        new_crop = Wheat()
    elif choice == 2:
        new_crop = Potato()
    return new_crop

def create_animal():
    display_menu_animal()
    choice = select_option([1,2])
    if choice == 1:
        name = input("What is this cow's name? ")
        new_animal = Cow(name)
    elif choice == 2:
        name = input("What is this sheep's name? ")
        new_animal = Sheep(name)
    return new_animal

def main():
    print("Will you be growing crops of livestock?")
    print()
    print("    1:   Crops    ")
    print("    2:   Livestock")
    print()
    choice = select_option([1,2])
    if choice == 1:
        new_crop = create_crop()
        manage_crop(new_crop)
    elif choice ==2:
        new_animal = create_animal()
        manage_animal(new_animal)


main()