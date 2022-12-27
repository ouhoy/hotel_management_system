import datetime

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', " "]
customer_details = {

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
    4: {"item": "roomTypeThree", "price": 35},
}
food_menu = {
    1: {"item": "ItemOne", "price": 12},
    2: {"item": "ItemTwo", "price": 82},
    3: {"item": "ItemThree", "price": 15},
    4: {"item": "ItemFour", "price": 18},
    5: {"item": "ItemFive", "price": 35},
    6: {"item": "ItemSix", "price": 23},
}


def name_validation(req):
    name = input(req).lower().strip()
    if len(name) > 512:
        print("name too long")
        return name_validation(req)
    if len(name) < 3:
        print("name too short")
        return name_validation(req)
    for element in name:
        if not element in alphabet:
            print(element)
            print("Make sure that your name does not contain any numbers or symbols.")
            return name_validation(req)
    return name


def date_validation(req, date_type="date"):
    date = input(req).strip().split("-")
    for n in date:
        if not n.isnumeric():
            print(f"Please, make sure that the {date_type} does not contain any characters or spaces.")
            return date_validation(req)
    if len(date[2]) != 4:
        print("Please put in the year in this format yyyy")
        return date_validation(req)
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    # If the used checked for an earlier date from today
    if "check-in" in customer_details:
        print("Working...")
        dates = datetime.date(year, month, day) - datetime.date(checkin_date["year"], checkin_date["month"],
                                                                checkin_date["day"])
        if 0 > dates.days:
            print(f"Enter a valid {date_type} up to one day from today")
            return date_validation(req)
    try:
        date_calc = datetime.date.today() - datetime.date(year, month, day)
        if date_calc.days > 0:
            print(datetime.date.today())
            print(datetime.date(year, month, day))
            print(f"Enter a valid {date_type} up to one day from today")
            return date_validation(req)

    except Exception as e:
        print(e)
        return date_validation(req)
    return {"day": day, "month": month, "year": year}


def num_input_validation(req, rng=range(0)):
    num = input(req).strip()
    if num.isnumeric():

        if len(rng) > 0 and int(num) in rng:
            return int(num)
        elif not rng:
            return int(num)

    print("Please put a valid number")
    return num_input_validation(input_req, rng)


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
    room_price = room_types[chosen_item]["price"]
    chosen_room = room_types[chosen_item]["item"]

    # customer_details["chosen_room_type"] = chosen_room
    # bill["room_rent"] += customer_details["nights_spent"] * room_price

    return {"chosen_room": chosen_room, "room_price": room_price}


def get_food():
    # Print all the items in the menu
    print_priced_items(food_menu)
    chosen_item = num_input_validation(
        "Kindly make your selection by inputting a number between 1 and 6 from the food menu options provided: ",
        rng=range(1, 7))
    item_price = food_menu[chosen_item]["price"]

    # bill["restaurant"] += item_price
    # Print SM
    order_again = input(
        "If you would like to place another order, please type 'Y'. If not, please type 'N'.").strip().lower()
    if order_again == "y":
        get_food()

    return {"chosen_item": chosen_item, "item_price": item_price}


user_name = name_validation("Write customer's name: ")
customer_details["user_name"] = user_name
user_address = input("Write the customer's address: ")
customer_details["user_address"] = user_address
# Get and save the check-in and check-out dates
checkin_date = date_validation("Check-in date: ")
customer_details["check-in"] = checkin_date
checkout_date = date_validation("Check-out date: ")
customer_details["check-out"] = checkout_date

customer_details["nights_spent"] = (datetime.date(checkout_date["year"], checkout_date["month"],
                                                  checkout_date["day"]) - datetime.date(
    checkin_date["year"], checkin_date["month"], checkin_date["day"])).days

get_room = room_checkin()

print(get_room)
customer_details["chosen_room"] = get_room["chosen_room"]
customer_details["room_rent"] = customer_details["nights_spent"] * get_room["room_price"]
print(customer_details)


# Calc total
for expense in bill:
    total += expense
def calc_total_cost():
    pass
