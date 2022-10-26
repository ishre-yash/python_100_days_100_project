import art
import game_data
import random
import os

def checkFollowers(followersA, followersB, score):
  global dataA
  global dataB
  if followersA > followersB and choice == 'A':
      score += 1
      dataB = random.choice(game_data.data)
      os.system('clear')
      return score
  elif followersB > followersA and choice == 'B':
      score += 1
      dataA = dataB
      dataB= random.choice(game_data.data)
      os.system('clear')
      return score
  else:
      os.system('clear')
      print(art.logo)
      print(f"Sorry, that's wrong! Final score: {score}")
      return False

score = 0
next = True
dataA = random.choice(game_data.data)
dataB = random.choice(game_data.data)
nameA = dataA['name']
followersA = dataA['follower_count']
descriptionA = dataA['description']
countryA = dataA['country']
nameB = dataB['name']
followersB = dataB['follower_count']
descriptionB = dataB['description']
countryB = dataB['country']

while(next):
  print(art.logo)
  if score > 0:
    nameA = dataA['name']
    followersA = dataA['follower_count']
    descriptionA = dataA['description']
    countryA = dataA['country']
    nameB = dataB['name']
    followersB = dataB['follower_count']
    descriptionB = dataB['description']
    countryB = dataB['country']
    print(f"You're right! Currect score : {score}")
  
  print(f"Compare A: {nameA}, a {descriptionA}, from {countryA}.")
  print(art.vs)
  print(f"Compare B: {nameB}, a {descriptionB}, from {countryB}.")
  print(f"FollowerA : {followersA}\t FollowerB : {followersB}")
  choice = input("Who has more followers? Type 'A' or 'B': ")
  score = checkFollowers(followersA, followersB, score)
  if score == 0:
    next = False
