import random
logo =
"""

  /$$$$$$                                                 /$$     /$$                       /$$   /$$                         /$$                                
 /$$__  $$                                               | $$    | $$                      | $$$ | $$                        | $$                                
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$       /$$$$$$  | $$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$       
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/      |_  $$_/  | $$__  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$      
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$         | $$    | $$  \ $$| $$$$$$$$      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/      
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$        | $$ /$$| $$  | $$| $$_____/      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$            
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/        |  $$$$/| $$  | $$|  $$$$$$$      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$            
 \______/  \______/  \_______/|_______/|_______/          \___/  |__/  |__/ \_______/      |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/            
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                                                                                                 

"""
def guess(number, level):
  for attempts in range(level,0,-1):
    print(f"You have {attempts} attempts remanining to guess the number.")
    userGuess = int(input("Make a guess: "))
    if userGuess == number:
      print(f"You got it! The answer was {number}")
      break
    elif userGuess > number:
      print("Too high.")
    elif userGuess < number:
      print("Too low.")
    print("Guess again.")
    
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
number = random.randint(1,101)
print(f"The corect answer is {number}")
choice = input("Chose a difficulty Type 'easy' or 'hard' :\n")
if choice == 'easy':
  guess(number, 10)
else:
  guess(number, 5)