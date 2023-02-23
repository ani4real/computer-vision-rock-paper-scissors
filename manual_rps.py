import random
option = ['rock','paper','scissors']

def get_computer_choice():
    computer_choice = random.choice(option)
    return computer_choice

def get_user_choice():
    while True:
        user_choice = input('Please enter your choice: ')
        if user_choice not in option:
            print("Please enter a valid choice.")
            user_choice = user_choice.lower()
        else:
            break
    return user_choice

        

def get_winner(computer_choice, user_choice):
    result = 0

    if computer_choice == user_choice:
        result = f"You've tied! you and the computer went with {computer_choice.upper()}!"
        
   
    elif computer_choice == 'rock' and user_choice == 'scissors':
        result = f"{computer_choice.upper()} beats {user_choice.upper()}. You've lost!"
        
    
    elif computer_choice == 'scissors' and user_choice == 'paper':
        result = f"{computer_choice.upper()} beats {user_choice.upper()}. You've lost!"
       

    elif computer_choice == 'paper' and user_choice == 'rock':
        result = f"{computer_choice.upper()} beats {user_choice.upper()}. You've lost!"
       
   
    elif computer_choice == 'rock' and user_choice == 'paper':
        result = f"{user_choice.upper()} beats {computer_choice.upper()}. You've won!"
        
    elif computer_choice == 'paper' and user_choice == 'scissors':
        result = f"{user_choice.upper()} beats {computer_choice.upper()}. You've won!"
       
    
    elif computer_choice == 'scissors' and user_choice == 'rock':
        result = f"{user_choice.upper()} beats {computer_choice.upper()}. You've won!"
        return result
    
    print(result) 
    

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)
    
play()
