def num_input_validation(input_req, rng=False):
    num = input(input_req)
    if num.isnumeric():
        num = int(num)
        if rng and num in rng:
            return int(num)
        elif not rng:
            return int(num)

    print("Please put a valid number")
    return num_input_validation(input_req, rng)


bill = {
    "restaurant": 0
}

x = 0

while 3 > x:
    x += 1

    def get_food():
        food_menu = {
            1: {"name": "ItemOne", "price": 12},
            2: {"name": "ItemTwo", "price": 82},
            3: {"name": "ItemThree", "price": 15},
            4: {"name": "ItemFour", "price": 18},
            5: {"name": "ItemFive", "price": 35},
            6: {"name": "ItemSix", "price": 23},
        }

        for key, value in food_menu.items():
            print(f'{key}) {value["name"]} - ${value["price"]}')
        chosen_item = num_input_validation("Please choose an item from the list. Put in a number between 1 to 6: ",
                                           range(1, 7))
        item_price = food_menu[chosen_item]["price"]
        bill["restaurant"] += item_price
        return item_price


    get_food()

print("bills ", bill["restaurant"])
