import requests
from colorizer import *

class Activity():
    def __init__(self):
        self.activity_name = ''
        self.activity_type = ''
        self.activity_participants = -1
        self.activity_price = -1
        self.activity_link = ''
        
    
    def get_activity(self, minprice = 0, maxprice = 0):
        resposne = requests.get(f"http://www.boredapi.com/api/activity?{minprice}=0&{maxprice}=0.1")

        if not resposne.ok:
            return False
        data = resposne.json()

        self.activity_name = data['activity']
        self.activity_type = data['type']
        self.activity_participants = data['participants']
        self.activity_price = data['price']
        self.activity_link = data['link']
        
        
        return True

    def show_activity(self):

        return f"""
{print_blue(f"What to do: {self.activity_name}")}
{print_red(f"Type of activity: {self.activity_type}")}
{print_yellow(f"How many persons do you need: {self.activity_participants if self.activity_participants != 1 else 'You and you and only you'}")}
{print_green(f"Price: ${self.activity_price * 100}")}
{print_cyan(f"Website: {self.activity_link if self.activity_link != '' else 'Don`t know how? - GOOOOOOOOOGLE IT'}")}
        """

