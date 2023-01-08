import datetime
import os
import re

art = """
  _    _       _       _                                                               _                   _                 
 | |  | |     | |     | |                                                             | |                 | |                
 | |__| | ___ | |_ ___| |  _ __ ___   __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_   ___ _   _ ___| |_ ___ _ __ ___  
 |  __  |/ _ \| __/ _ \ | | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __| / __| | | / __| __/ _ \ '_ ` _ \ 
 | |  | | (_) | ||  __/ | | | | | | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_  \__ \ |_| \__ \ ||  __/ | | | | |
 |_|  |_|\___/ \__\___|_| |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__| |___/\__, |___/\__\___|_| |_| |_|
                                                        __/ |                                     __/ |                      
                                                       |___/                                     |___/                       
"""
print(art)


def check_email(prompt_string: str) -> str:
    email = input(prompt_string)
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pat, email):
        return email
    else:
        print("Please enter a valid email.")
        return check_email(prompt_string)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Bcolors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


customer_details = {
    "stay_duration": 0,
    "nights_spent": 0,
    "ordered_food": [],
    "laundry": []

}
ROOM_SERVICE_COST_PER_DAY = 2

# TODO follow the data:
bill = {
    "room_rent": 0,
    "room_service": 0,
    "restaurant": 0,
    "restaurant_tips": 0,
    "laundry": 0,
    "game": 0,
    "TAX": 0

}

total = 0
# TODO: 3) fix lang
# TODO: 3) Add a room number

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


# Data validation functions

# TODO color error validation

def name_validation(prompt_string: str) -> str:
    name = input(prompt_string).lower().strip()

    # Check if name is empty
    if not name:
        print("Please enter a valid name")
        return name_validation(prompt_string)

    # Check if name includes alphabetical characters only
    if not name.replace(" ", "").isalpha():
        print("Make sure that your name does not contain any numbers or symbols.")
        return name_validation(prompt_string)

    # Check the length of the name
    if len(name) > 64:
        print("The entered name is too long, please enter a valid name that doe not exceed 64 characters in count.")
        return name_validation(prompt_string)
    if len(name) < 1:
        print("The entered name is too short, please enter a valid name that doe not go under 1 character in count.")
        return name_validation(prompt_string)

    return name


# TODO color error validation
def date_validation(prompt_string: str, date_type: str, checkin_date: datetime = None) -> datetime:
    date = input(prompt_string).strip().split("-")
    year_expected_length = 4

    # Validate inputs' data type
    for n in date:
        if not n.isnumeric():
            print(
                f"{Bcolors.WARNING}Please, make sure that the {date_type} does not contain any characters or spaces. {Bcolors.END}")
            return date_validation(prompt_string, date_type, checkin_date)

    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    # Check if the entered year follows the format of YYYY
    if len(str(year)) != year_expected_length:
        print("Please put in the year in this format yyyy")
        return date_validation(prompt_string, date_type, checkin_date)

    # If the user checked for an earlier check-out date from the check-in date
    # TODO check stay duration
    if date_type == "check-out":
        try:
            dates = datetime.date(year, month, day) - checkin_date
            if 0 > dates.days:
                print(f"Enter a valid date at least one day from the check-in date: {checkin_date}")
                return date_validation(prompt_string, date_type, checkin_date)
        except Exception as e:
            print(e)
            return date_validation(prompt_string, date_type, checkin_date)
    try:
        date_calc = datetime.date.today() - datetime.date(year, month, day)

        # If the user checked for an earlier date from the current date
        if date_calc.days > 0:
            print(f"Enter a valid date up to one day from today")
            return date_validation(prompt_string, date_type, checkin_date)
    except Exception as e:
        print(e)
        return date_validation(prompt_string, date_type, checkin_date)
    return datetime.date(year, month, day)


# TODO color error validation
def num_input_validation(prompt_string: str, ls: range or list) -> int:
    num = input(prompt_string).strip()

    # Check if the entered number is numeric and is in the list
    if num.isnumeric():
        if ls and int(num) in range(1, len(ls) + 1):
            return int(num) - 1
        elif not ls:
            return int(num)

    print(f"Please put a valid number")
    return num_input_validation(prompt_string, ls)


def select_again(prompt_string: str) -> bool:
    selection = input(
        f"{Bcolors.INFO}{prompt_string} If yes type Y otherwise hit enter to continue: {Bcolors.END}").strip().lower()
    if selection == "y":
        return True
    return False


def print_priced_items(ls: list):
    for item in range(len(ls)):
        print(f'{item + 1}) {ls[item]["item"]} - ${ls[item]["price"]}')


# Hotel services functions
def room_checkin() -> dict:
    print("Our luxurious accommodations include a selection of four opulent room types to choose from: ")
    print_priced_items(room_types)
    chosen_item = num_input_validation(
        "In order to make your selection, please input a number between 1 and 4 corresponding to the "
        "desired room type from the list: ",
        ls=room_types)

    # Confirm user choice
    print("You have selected: ")
    print(f'Chosen Room Type: {room_types[chosen_item]["item"]}')
    print(f'Price per night: ${room_types[chosen_item]["price"]}')
    if select_again("Do you want to edit your inputs? "):
        return room_checkin()

    # Room bill
    print("** Rent Details **")
    print(f'Chosen Room Type: {room_types[chosen_item]["item"]}')
    print(f'Price per night: ${room_types[chosen_item]["price"]}')
    print(f'Stay duration: {customer_details["stay_duration"]} days')
    print(f'Total:, ${room_types[chosen_item]["price"] * customer_details["stay_duration"]} ')
    return room_types[chosen_item]


def get_food() -> dict:
    # Print all the items in the menu
    print_priced_items(food_menu)
    chosen_item = num_input_validation(
        f"Kindly make your selection by inputting a number between 1 and {len(food_menu)} from the food menu options provided: ",
        ls=food_menu)

    # Confirm user choice
    print("You have selected: ")
    print(f"Chosen dish: {food_menu[chosen_item]['item']} - ${food_menu[chosen_item]['price']}")
    if select_again("Do you want to edit your inputs? "):
        return get_food()

    # The print the bill
    print("** Restaurant Bill **")
    print(f"Chosen dish: {food_menu[chosen_item]['item']} ")
    print(f"Total: ${food_menu[chosen_item]['price']} ")

    return food_menu[chosen_item]
    # TODO: 1)  Don't forget the tep as an additional charge


def laundry() -> dict:
    print("We offer four types of laundry")
    print_priced_items(laundry_types)
    chosen_laundry_type = num_input_validation(
        f"Please enter the number of the desired laundry type from 1 to {len(laundry_types)}: ", laundry_types)
    quantity = num_input_validation("Please enter the desired laundry quantity nothing above 20: ", range(1, 21)) + 1
    price = laundry_types[chosen_laundry_type]["price"] * quantity

    print("You have selected: ")
    print(f"Chosen laundry type: {laundry_types[chosen_laundry_type]['item']} ")
    print(f"quantity: {quantity} ")
    if select_again("Do you want to edit your inputs? "):
        return laundry()
    # Laundry bill
    print("** Laundry Bill **")
    print(f"Chosen laundry type: {laundry_types[chosen_laundry_type]['item']} ")
    print(f"quantity: {quantity} ")
    print(f"Total: ${price} ")

    return {"type": laundry_types[chosen_laundry_type], "quantity": quantity, "price": price}


def game():
    pass


def get_customer_data() -> dict:
    guest_first_name = name_validation("Enter your first name: ")
    guest_last_name = name_validation("Enter your last name: ")

    user_address = input(
        "Enter your address, including the street, city, state/province, and country in one line: ").strip()

    # Validate user address
    while len(user_address) < 3 or len(user_address) > 170:
        print("Please enter a valid address that is between 3 and 170 characters.")
        user_address = input("Please enter your address, including the street, city, and state/province in one line: ")
    email_address = check_email("Enter your email address: ")

    checkin_date = date_validation("Please enter the check-in date following this format dd-mm-yyyy: ", "check-in")
    checkout_date = date_validation("Please enter the check-out date following this format dd-mm-yyyy: ", "check-out",
                                    checkin_date)
    stay_duration = (checkout_date - checkin_date).days

    cls()

    print("\n** Customer's entered data **\n")
    print(f"Customer First Name: {guest_first_name}")
    print(f"Customer Last Name: {guest_last_name}")
    print(f"Customer Address: {user_address}")
    print(f"Check-in Date: {checkin_date.day}-{checkin_date.month}-{checkin_date.year}")
    print(f"Check-out Date: {checkout_date.day}-{checkout_date.month}-{checkout_date.year}")

    if select_again("Do you want to edit your personal information? "):
        return get_customer_data()

    user_collected_data = {"first_name": guest_first_name, "last_name": guest_last_name, "user_address": user_address,
                           "email_address": email_address,
                           "checkin_date": checkin_date,
                           "checkout_date": checkout_date, "stay_duration": stay_duration}

    return user_collected_data


customer_data = get_customer_data()
cls()
customer_details.update(customer_data)

##### Functional Area #####

# Get a room:
get_room = room_checkin()
cls()
customer_details["chosen_room"] = get_room
customer_details["room_rent"] = customer_details["stay_duration"] * get_room["price"]
bill["room_rent"] = customer_details["stay_duration"] * get_room["price"]
bill["room_service"] = customer_details["nights_spent"] * ROOM_SERVICE_COST_PER_DAY

while True:
    # TODO fix lang here
    user_functions = ["Order food", "Do laundry", "Print the bill"]
    for i in range(len(user_functions)):
        print(f"{i + 1}) {user_functions[i]} ")
    service = num_input_validation("Get served: ", user_functions)

    # Order food
    if service == 0:
        ordered_food = get_food()
        customer_details["ordered_food"].append(ordered_food)
        bill["restaurant"] += ordered_food["price"]
        if select_again("Would you like to order again? "):
            ordered_food = get_food()
            customer_details["ordered_food"].append(ordered_food)
            bill["restaurant"] += ordered_food["price"]
        continue

    # Do laundry
    if service == 1:
        laundry_service = laundry()
        customer_details["laundry"].append(laundry_service)
        bill["laundry"] += laundry_service["price"]
        continue

    if service == 2:
        break

for expense in bill:
    total += bill[expense]


def print_total_cost():
    # Customer details
    print("\n**** Customer details ****\n")
    print("Customer First Name: ", customer_details["first_name"])
    print("Customer Last Name: ", customer_details["last_name"])
    print("Customer Address: ", customer_details["user_address"])
    print(
        f"Check-in Date: {customer_details['checkin_date'].day}-{customer_details['checkin_date'].month}-{customer_details['checkin_date'].year}")
    print(
        f"Check-out Date: {customer_details['checkout_date'].day}-{customer_details['checkout_date'].month}-{customer_details['checkout_date'].year}")
    # TODO fix this
    print("Chosen Room Type: ", customer_details["chosen_room"])
    print("Number of nights spent: ", customer_details["stay_duration"])
    # Customer's Bill
    print("\n**** Customer's Bill ****\n")

    # room
    print("Room rent: ", bill["room_rent"])
    print("Room service: ", bill["room_service"])
    # restaurant
    print("\nRestaurant bill: ")
    for order in customer_details["ordered_food"]:
        print(f"-{order['item']}, {order['price']}. ")
    print("Restaurant total: ", bill["restaurant"])

    # laundry
    print("\nLaundry bill: ")
    for item in customer_details["laundry"]:
        # TODO: Fix this:
        print(item)
        # print(f"-{item['item']}, {item['price']}. ")
    print("Laundry total: ", bill["laundry"])
    # Total
    print(f"\nYour total is: ", total)


print_total_cost()
