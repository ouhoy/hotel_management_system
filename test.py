customer_details = {
    "nights_spent": 0,
    "ordered_food": [],
    "laundry": []
}

bill = {
    "room_rent": 0,
    "restaurant": 0,
    "laundry": 0,
    "game": 0,
    "TAX": 0

}

total = 0

room_types = {
    1: {"item": "roomTypeOne", "price": 8},
    2: {"item": "roomTypeTwo", "price": 15},
    3: {"item": "roomTypeThree", "price": 24},
    4: {"item": "roomTypeFour", "price": 35},
}
food_menu = {
    1: {"item": "ItemOne", "price": 12},
    2: {"item": "ItemTwo", "price": 82},
    3: {"item": "ItemThree", "price": 15},
    4: {"item": "ItemFour", "price": 18},
    5: {"item": "ItemFive", "price": 35},
    6: {"item": "ItemSix", "price": 23},
}

laundry_types = {
    1: {"item": "Normal laundry", "price": 2},
    2: {"item": "Special laundry", "price": 4},
    3: {"item": "Uniform laundry", "price": 10},
}


def name_validation(prompt_string):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', " "]
    name = input(prompt_string).lower().strip()
    if len(name) > 512:
        print("name too long")
        return name_validation(prompt_string)
    if len(name) < 3:
        print("name too short")
        return name_validation(prompt_string)
    for element in name:
        if not element in alphabet:
            print(element)
            print("Make sure that your name does not contain any numbers or symbols.")
            return name_validation(prompt_string)
    return name


def num_input_validation(prompt_string, rng=range(0)):
    num = input(prompt_string).strip()
    if num.isnumeric():

        if len(rng) > 0 and int(num) in rng:
            return int(num)
        elif not rng:
            return int(num)

    print("Please put a valid number")
    return num_input_validation(prompt_string, rng)


def print_priced_items(ls):
    for key, value in ls.items():
        print(f'{key}) {value["item"]} - ${value["price"]}')


def room_checkin():
    print("Our luxurious accommodations include a selection of four opulent room types to choose from: ")
    print_priced_items(room_types)
    chosen_item = num_input_validation(
        "In order to make your selection, please input a number between 1 and 4 corresponding to the "
        "desired room type from the list.",
        rng=range(1, 5))

    return room_types[chosen_item]


def laundry():
    print("We offer four types of laundry")
    print_priced_items(laundry_types)
    chosen_laundry_type = num_input_validation("Please enter the desired laundry type: ", range(1, 4))
    weight = num_input_validation("Please enter the desired laundry weight nothing above 5kg: ", range(1, 5))
    price = laundry_types[chosen_laundry_type]["price"] * weight
    print(f"Chosen laundry type: {laundry_types[chosen_laundry_type]['item']} ")
    print(f"Weight: {weight}kg ")
    print(f"Total: ${price} ")
    return {"type": laundry_types[chosen_laundry_type], "weight": weight, "price": price}


def get_food():
    # Print all the items in the menu
    print_priced_items(food_menu)
    chosen_item = num_input_validation(
        "Kindly make your selection by inputting a number between 1 and 6 from the food menu options provided: ",
        rng=range(1, 7))
    return food_menu[chosen_item]


# Get room

# Get food
# customer_details["ordered_food"].append(get_food())
# Do laundry
laundry_service = laundry()
customer_details["laundry"].append(laundry())
print("Here it worked")
bill["laundry"] += laundry_service["price"]
print("Here it is done")

print(customer_details)

print("Test form GitHub")
