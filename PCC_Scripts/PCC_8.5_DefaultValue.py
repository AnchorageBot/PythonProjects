# This function will use a default pet value unless otherwise defined - default value example

# Source code/inspiration/software
    # Python Crash Course by Eric Matthews, Chapter 8, example 5+
    # Made with Mu 1.0.3 in October 2021

def describe_pet(pet_name, animal_type='dog'):
    """Display info about a pet using a default value"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('del')
describe_pet(pet_name='doug')
describe_pet(pet_name='carl',animal_type='cat')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('sam','snake')
