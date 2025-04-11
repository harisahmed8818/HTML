import json 
import os 
import datetime

class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price 
        self.is_available = True 
        self.guest_name = None
        self.check_in_date = None

    def book_room(self, guest_name):
        if self.is_available:
            self.is_available = False
            self.guest_name = guest_name
            self.check_in_date = datetime.date.today()
            print(f"Room{self.room_number} has been booked for {guest_name}.")
        else:
            print(f"Room{self.room_number} is already booked.")

    def check_out(self):
        if not self.is_available:
            self.is_available = True
            self.guest_name = None 
            self.check_in_date = None
            print(f"Room{self.room_number} is now available.")
