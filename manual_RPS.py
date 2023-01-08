import random
option = ['Rock','Paper','Scissors']


def get_computer_choice():
    computer_choice = random.choice(option)
    return computer_choice

def get_user_choice():
    user_choice = input('Please enter your choice')
    return user_choice
    