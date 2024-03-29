import pdb
# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def add_or_remove_cash(pet_shop, cash):
    pet_shop['admin']['total_cash'] += cash

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def get_stock_count(pet_shop):
    return len(pet_shop['pets'])

def get_pets_by_breed(pet_shop, pet_name):
    pets = []

    for pet in pet_shop['pets']:
        if pet['breed'] == pet_name:
            pets.append(pet)
    return pets

def increase_pets_sold(pet_shop, number_sold):
    pet_shop['admin']['pets_sold'] += number_sold

def remove_pet_by_name(pet_shop, pet_name):
    pets = pet_shop['pets']
    for pet in pets:
        if pet['name'] == pet_name:
            pets.remove(pet)
            return

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop['pets'].append(new_pet)

def get_customer_cash(customer_cash):
    return customer_cash['cash']

def remove_customer_cash(customer_cash, amount):
    customer_cash['cash'] -= amount

def get_customer_pet_count(customer_pet):
    return len(customer_pet['pets'])

def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)

 # --- OPTIONAL ---

def customer_can_afford_pet(customer, pet):
    return customer['cash'] >= pet['price']

 # --- Integration ---

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet) == True:
        add_or_remove_cash(pet_shop, pet["price"])
        remove_customer_cash(customer, pet["price"])
        increase_pets_sold(pet_shop, 1)
        add_pet_to_customer(customer, pet)
