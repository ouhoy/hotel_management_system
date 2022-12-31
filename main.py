import datetime

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

# TODO: 3) fix lang here
room_types = [{"item": "roomTypeOne", "price": 8},
              {"item": "roomTypeTwo", "price": 15},
              {"item": "roomTypeThree", "price": 24},
              {"item": "roomTypeFour", "price": 35}, ]
food_menu = [{"item": "ItemOne", "price": 12},
             {"item": "ItemTwo", "price": 82},
             {"item": "ItemThree", "price": 15},
             {"item": "ItemFour", "price": 18},
             {"item": "ItemFive", "price": 35},
             {"item": "ItemSix", "price": 23}, ]
laundry_types = [{"item": "Normal laundry", "price": 2},
                 {"item": "Special laundry", "price": 4},
                 {"item": "Uniform laundry", "price": 10}, ]


def name_validation(prompt_string):
    name = input(prompt_string).lower().strip()
    if len(name) > 512:
        print("name too long")
        return name_validation(prompt_string)
    if len(name) < 3:
        print("name too short")
        return name_validation(prompt_string)
    if not name.replace(" ", "").isalpha():
        print("Make sure that your name does not contain any numbers or symbols.")
        return name_validation(prompt_string)
    return name


def date_validation(prompt_string, date_type="date"):
    date = input(prompt_string).strip().split("-")
    for n in date:
        if not n.isnumeric():
            print(f"Please, make sure that the {date_type} does not contain any characters or spaces.")
            return date_validation(prompt_string)
    if len(date[2]) != 4:
        print("Please put in the year in this format yyyy")
        return date_validation(prompt_string)
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    # If the used checked for an earlier date from today
    if "check-in" in customer_details:
        try:

            dates = datetime.date(year, month, day) - datetime.date(checkin_date["year"], checkin_date["month"],
                                                                    checkin_date["day"])
            if 0 > dates.days:
                print(f"Enter a valid {date_type} up to one day from today")
                return date_validation(prompt_string)
        except Exception as e:
            print(e)
            return date_validation(prompt_string)
    try:
        date_calc = datetime.date.today() - datetime.date(year, month, day)
        if date_calc.days > 0:
            print(f"Enter a valid {date_type} up to one day from today")
            return date_validation(prompt_string)
    except Exception as e:
        print(e)
        return date_validation(prompt_string)
    return {"day": day, "month": month, "year": year}


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
    for item in range(len(ls)):
        print(f'{item + 1}) {ls[item]["item"]} - ${ls[item]["price"]}')


def room_checkin():
    print("Our luxurious accommodations include a selection of four opulent room types to choose from: ")
    print_priced_items(room_types)
    chosen_item = num_input_validation(
        "In order to make your selection, please input a number between 1 and 4 corresponding to the "
        "desired room type from the list.",
        rng=range(1, len(room_types) + 1))
    # TODO: 2) Don't forget the room service as an additional charge
    return room_types[chosen_item - 1]


def get_food():
    # Print all the items in the menu
    print_priced_items(food_menu)
    chosen_item = num_input_validation(
        "Kindly make your selection by inputting a number between 1 and 6 from the food menu options provided: ",
        rng=range(1, len(food_menu) + 1))
    return food_menu[chosen_item - 1]
    # TODO: 1)  Don't forget the tep as an additional charge


def laundry():
    print("We offer four types of laundry")
    print_priced_items(laundry_types)
    chosen_laundry_type = num_input_validation("Please enter the desired laundry type: ",
                                               range(1, len(laundry_types) + 1))
    quantity = num_input_validation("Please enter the desired laundry quantity: ")
    price = laundry_types[chosen_laundry_type]["price"] * quantity

    print(f"Chosen laundry type: {laundry_types[chosen_laundry_type]['item']} ")
    print(f"quantity: {quantity} ")
    print(f"Total: ${price} ")

    return {"type": laundry_types[chosen_laundry_type], "quantity": quantity, "price": price}


def game():
    pass


customer_details["user_name"] = name_validation("Write customer's name: ")
customer_details["user_address"] = input("Write the customer's address: ")

# Get and save the check-in and check-out dates
checkin_date = date_validation("Check-in date: ")
customer_details["check-in"] = checkin_date
checkout_date = date_validation("Check-out date: ")
customer_details["check-out"] = checkout_date

customer_details["nights_spent"] = (datetime.date(checkout_date["year"], checkout_date["month"],
                                                  checkout_date["day"]) - datetime.date(
    checkin_date["year"], checkin_date["month"], checkin_date["day"])).days

##### Functional Area #####
# Get room:
get_room = room_checkin()
customer_details["chosen_room"] = get_room
customer_details["room_rent"] = customer_details["nights_spent"] * get_room["price"]
bill["room_rent"] = customer_details["nights_spent"] * get_room["price"]

while True:
    user_functions = ["Order food", "Do laundry", "Print the bill"]
    for i in range(len(user_functions)):
        print(f"{i + 1}) {user_functions[i]} ")
    service = num_input_validation("Get served: ", range(1, len(user_functions) + 1))

    # Order food
    if service == 1:
        ordered_food = get_food()
        customer_details["ordered_food"].append(ordered_food)
        bill["restaurant"] += ordered_food["price"]

    # Do laundry
    if service == 2:
        laundry_service = laundry()
        customer_details["laundry"].append(laundry_service)
        bill["laundry"] += laundry_service["price"]
    if service == 3:
        break

# Calc total

# for food in customer_details["ordered_food"]:
#     bill["restaurant"] += food["price"]
#
# for washed in customer_details["laundry"]:
#     bill["laundry"] += washed["price"]

for expense in bill:
    total += bill[expense]


def print_total_cost():
    # Customer details
    print("**** Customer details ****")
    print("Customer Name: ", customer_details["user_name"])
    print("Customer Address: ", customer_details["user_address"])
    print("Check-in Date: ", customer_details["check-in"]["day"], customer_details["check-in"]["month"],
          customer_details["check-in"]["year"])
    print("Check-out Date: ", customer_details["check-out"]["day"], customer_details["check-out"]["month"],
          customer_details["check-out"]["year"])
    print("Chosen Room Type: ", customer_details["chosen_room"])
    print("Number of nights spent: ", customer_details["nights_spent"])
    # Customer's Bill
    print("**** Customer's Bill ****")

    # room
    print("Room rent: ", bill["room_rent"])
    # restaurant
    print("Restaurant bill: ")
    for order in customer_details["ordered_food"]:
        print(f"-{order['item']}, {order['price']}. ")
    print("Restaurant total: ", bill["restaurant"])

    # laundry
    print("Laundry bill: ")
    for item in customer_details["laundry"]:
        print(item)
        # print(f"-{item['item']}, {item['price']}. ")
    print("Laundry total: ", bill["laundry"])
    # Total
    print(f"Your total is: ", total)


print(customer_details)
print(total)
print_total_cost()
