import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
def calculate_score(lists):
  score = sum(lists)
  if 10 in lists and 11 in lists and len(lists)==2:
    return 0 #blackjack
  if 11 in lists and score > 21:
    lists.remove(11)
    lists.append(1)
  return sum(lists)
def compare(user, computer):
  if user > 21 and computer > 21:
      print("You went over. You lose 😤")
  if user == computer:
    print("It's Draw")
  elif computer == 0:
    print("Lose, opponent has Blackjack 😱")
  elif user == 0:
    print("Win with a Blackjack 😎")
  elif user > 21:
    print("You went over. You lose 😭")
  elif computer > 21:
    print("Opponent went over. You win 😁")
  elif user > computer:
    print("You win 😃")
  else:
    print("You lose!")
  
while(input("Do You want to play a game of blackjack,Type 'y' or 'n'") == 'y'):
  print(logo)
  end = True
  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while(end):
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your card: {user_cards},current score:{user_score} ")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 and computer_score == 0 and user_score > 21:
      end = False
    else:
      next_card = input("Type 'y' to get another card, type 'n' to pass:")
      if next_card == 'y':
        user_cards.append(deal_card())
        if computer_score < 17:
          computer_cards.append(deal_card())
      else:
        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
        compare(user_score, computer_score)
        end = False  