import datetime

customer_details = {
}
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', " "]
bill = {
    "room_rent": 0,
    "restaurant": 0,
    "laundry": 0,
    "game": 0,
    "TAX": 0

}
user_name = input("Write customer's name: ")
user_address = input("Write the customer's address: ")
checkin_date = input("Check-in date: ")
checkout_date = input("Check-out date: ")


def name_validation(name):
    if len(name) > 512:
        print("name too long")
        return
    if len(name) < 3:
        print("name too short")
        return
    for element in user_name:
        if not element in alphabet:
            print("Please put in a valid name")
            print(element)
    return name


def date_validation(date):
    date = date.split("-")
    day = date[0]
    month = date[1]
    year = date[2]
    for num in date:
        if not num.isnumeric():
            print("not valid")
            return

    if 10 < len(date) < 6:
        print("Not valid")
        return

    if not ((len(day) > 2 or len(day) == 0) or (len(month) > 2 or len(month) == 0) or (
            len(year) < 2 or len(year) == 3 or len(year) > 4)):
        if len(year) == 2:
            if int(year) < 22:
                print("Put in a valid date")
                return
        if len(year) == 4:
            if int(year) < 2022:
                print("Put in a valid date")
                return
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        try:
            return datetime.datetime(year, month, day)

        except Exception as e:
            print(e)

        print("Not valid")
        return
#
# room_types = {
#     1: {"item": "roomTypeOne", "price": 8},
#     2: {"item": "roomTypeTwo", "price": 15},
#     3: {"item": "roomTypeThree", "price": 24},
#     4: {"item": "roomTypeThree", "price": 35},
# }
#
#
# def checkin_type():
#     print("Our luxurious accommodations include a selection of four opulent room types to choose from: ")
#     print_priced_items(room_types)
#     chosen_item = num_input_validation(
#         "In order to make your selection, please input a number between 1 and 4 corresponding to the "
#         "desired room type from the list.",
#         rng=range(1, 4))
#     item_price = room_types[chosen_item]["price"]
#     bill["room_rent"] += item_price
#     return item_price
#
#
# def num_input_validation(input_req, rng=False):
#     num = input(input_req).strip()
#     if num.isnumeric():
#         num = int(num)
#         if rng and num in rng:
#             return int(num)
#         elif not rng:
#             return int(num)
#
#     print("Please put a valid number")
#     return num_input_validation(input_req, rng)
#
#
# def print_priced_items(ls):
#     for key, value in ls.items():
#         print(f'{key}) {value["item"]} - ${value["price"]}')
#
#
# def get_food():
#     food_menu = {
#         1: {"item": "ItemOne", "price": 12},
#         2: {"item": "ItemTwo", "price": 82},
#         3: {"item": "ItemThree", "price": 15},
#         4: {"item": "ItemFour", "price": 18},
#         5: {"item": "ItemFive", "price": 35},
#         6: {"item": "ItemSix", "price": 23},
#     }
#
#     # Print all the items in the menu
#     print_priced_items(food_menu)
#
#     chosen_item = num_input_validation(
#         "Kindly make your selection by inputting a number between 1 and 6 from the food menu options provided: ",
#         rng=range(1, 7))
#     item_price = food_menu[chosen_item]["price"]
#     bill["restaurant"] += item_price
#     return item_price
#
#
# get_food()
# checkin_type()
#
# print(bill)
