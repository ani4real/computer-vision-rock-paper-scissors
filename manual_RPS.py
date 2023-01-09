import random
option = ['Rock','Paper','Scissors']


def get_computer_choice():
    computer_choice = random.choice(option)
    return computer_choice

def get_user_choice():
    user_choice = input('Please enter your choice')
    if user_choice not in option:
            print("Please enter a valid choice")
    user_choice = user_choice.lower()
    return user_choice

def get_winner(computer_choice,user_choice):
    
    if computer_choice == user_choice():
        result = f"You've tied since the both the choices were {computer_choice}!"
   
    elif computer_choice == 'rock' and user_choice == 'scissor':
        result = f"{computer_choice} beats {user_choice}. You've lost!"
    
    elif computer_choice == 'scissor' and user_choice == 'paper':
        result = f"{computer_choice} beats {user_choice}. You've lost!"
   
    elif computer_choice == 'paper' and user_choice == 'rock':
        result = f"{computer_choice} beats {user_choice}. You've lost!"
   
    elif computer_choice == 'rock' and user_choice == 'paper':
        result = f"{user_choice} beats {computer_choice}. You've won!"

    elif computer_choice == 'paper' and user_choice == 'scissor':
        result = f"{user_choice} beats {computer_choice}. You've won!"
    
    elif computer_choice == 'scissors' and user_choice == 'rock':
        result = f"{user_choice} beats {computer_choice}. You've won!"

    return result
    
    