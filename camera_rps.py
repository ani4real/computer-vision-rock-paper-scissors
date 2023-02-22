import cv2
from keras.models import load_model
import numpy as np
import time
import random


class RPS:

    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape = (1, 224, 224, 3), dtype = np.float32)

    def get_countdown(self):
        countdown = 5
        print("\nBe prepared to show your choice in...")
        time.sleep(1)
        while countdown > 0:
            print(f'{countdown}-')
            cv2.waitKey(1000)
            countdown -= 1
        
        print('\nShow your hand now')   

    def get_prediction(self):
                
        end = time.time() + 1
        
        while time.time() < end:
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            cv2.imshow('frame', frame)
            prediction = self.model.predict(self.data)
            self.choice = choice_list[prediction.argmax()]
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return self.choice

    def get_computer_choice(self):
        computer_choice = random.choice(choice_list)
        return computer_choice

    def get_winner(self, computer_choice, user_choice):
        
        if user_choice == "nothing":
            print("Restart! Please pick an option")
            return

        elif computer_choice == user_choice:
            print(f"You've tied! you and the computer went with {computer_choice.upper()}!")
            
    
        elif computer_choice == 'rock' and user_choice == 'scissors':
            print(f"{computer_choice.upper()} beats {user_choice.upper()}. You've lost!")
            self.computer_wins += 1 
            
        
        elif computer_choice == 'scissors' and user_choice == 'paper':
            print(f"{computer_choice.upper()} beats {user_choice.upper()}. You've lost!")
            self.computer_wins += 1 

        elif computer_choice == 'paper' and user_choice == 'rock':
            print(f"{computer_choice.upper()} beats {user_choice.upper()}. You've lost!")
            self.computer_wins += 1 
    
        elif computer_choice == 'rock' and user_choice == 'paper':
            print(f"{user_choice.upper()} beats {computer_choice.upper()}. You've won!")
            self.user_wins += 1 
            
        elif computer_choice == 'paper' and user_choice == 'scissors':
            print(f"{user_choice.upper()} beats {computer_choice.upper()}. You've won!")
            self.user_wins += 1
        
        elif computer_choice == 'scissors' and user_choice == 'rock':
            print(f"{user_choice.upper()} beats {computer_choice.upper()}. You've won!")
            self.user_wins += 1
            
def play_game(choice_list):
    R1 = RPS()
    print('Welcome to the ROCK, PAPER, SCISSORS game')
    enter = input('press y to begin')
    if enter == 'y':
        while True:
            
            R1.get_countdown()
            computer_choice = R1.get_computer_choice()
            user_choice = R1.get_prediction()

            if user_choice == 'Nothing':
                print('Please make a choice')
                break
            else:
                R1.get_winner(computer_choice, user_choice)
            
                if R1.computer_wins == 3:
                    print("You lost the game!")
                    break
                elif R1.user_wins == 3:
                    print("You won the game!")
                    break
         # After the loop release the cap object

        RPS.cap.release()

        # Destroy all the windows

        cv2.destroyAllWindows()
    
    else:
        print('you have quit the game')



if __name__ == "__main__":
    choice_list = ["Rock", "Paper", "Scissors", "Nothing"]
    play_game(choice_list)