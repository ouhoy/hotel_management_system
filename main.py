# user_name = input("What is your name ").strip()
# user_address = input("What is you address ")
# checkin_date = input("When is your preferable check-in date? ")
# checkout_date = input("When is your preferable check-out date? ")
# print("There are 3 types of rooms in this hotel, please pick one in the menu.")
#
# room_type = input("")
# nights_spent_number = input("How many nights are you going to stay in here? ")


class User:
    def __init__(self, user_name, user_address):
        self.user_name = user_name
        self.user_address = user_address


class RoomRent:
    def __init__(self, room_type, checkin, checkout):
        self.room_type = room_type
        self.checkin = checkin
        self.checkout = checkout


class HotelServices:
    def __init__(self, service):
        self.service = service

