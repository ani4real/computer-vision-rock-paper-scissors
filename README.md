Rock-Paper-Scissors is a game played to settle disputes between two people. Thought to be a game of chance that depends on random luck similar to flipping coins. The game is played with three possible hand signals that represent a rock, paper, and scissors. The rock is a closed fist; paper is a flat hand with fingers and thumb extended and the palm facing downward; and scissors is a fist with the index and middle fingers fully extended toward the opposing player. Rock wins against scissors; paper wins against rock; and scissors wins against paper. If both players throw the same hand signal, it is considered a tie, and play resumes until there is a clear winner

# Description

This Python project is an implementation of the "Rock, Paper, Scissors" where the user plays with the computer using computer vision through a machine-learning model created with Teachable-Machine.

## Milestone 1 & 2

- In the first milestone a model was exported from Teachable Machine. Teachable machine is a web tool that makes it fast and easy to create machine learning models for projects, no coding required. Train a computer to recognize images, sounds, & poses.

The model was downloaded from the tensorflow tab. keras_model.h5 and labels.txt were the teo files that were extracted onto the local device. These contain the structure and the parameters of a deep learaning model.

## Milestone 3 
Milestone 3 was where where all the dependencies were installed from the command line. ```opencv-python```, ```tensorflow``` and ```ipykernel``` were the neccesary requirements that were installed. ```pip install``` command was used to install the libraries. A virtual environment called RPS-env was created where all the libraries were installed.

## Milestone 4
In milestone 4, The computer's and user's choice was picked using functions ```computer_choice()``` and ```user_choice()``` respectively. Then a function ```get_winner()``` was defined to code the logic of the game based on the inputs from the user and the computer. All the previous functions were wrapped in the ```play()``` function which allows to play the game with the computer without the camera. Run the camera_rps.py file if you wish to play with the computer without using the camera. 

## Milestone 5
Everything from the previous milestones were put together in milestone 5. The code from milestone 4 was wrapped in a class called 'RPS'. To use the camera the model in the ```get_prediction()``` was implemented on the code. The ```opencv-python``` module was implemented to use the camera. A ```get_coundown()``` was defined to get a timer started before the user is ready to show the choice. The countdown timer was set to 5 seconds. Once the timer goes off the camera is open and the user should show the camera choice that they want. Once the camera is open it takes the final image counts. Note that this method will return "nothing" if it cannot fit the image to rock / paper / scissors with a high probability from the model. 