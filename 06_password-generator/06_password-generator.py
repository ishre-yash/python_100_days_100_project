#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
total = nr_letters + nr_symbols + nr_numbers
passcoad = []
"""
for i in range(0,total):
  if i < nr_letters:
    passcoad.append(random.choice(letters))
for i in range(0,total):   
  if i < nr_symbols:
    passcoad.append(random.choice(symbols))
for i in range(0,total):
  if i < nr_numbers:
    passcoad.append(random.choice(numbers))
password = "".join(passcoad)
print(password.replace(" ", ""))
"""
#Hard Level - Order of characters randomised:
for i in range(0,total):
  if i < nr_letters:
    passcoad.append(random.choice(letters))
  if i < nr_symbols:
    passcoad.append(random.choice(symbols))
  if i < nr_numbers:
    passcoad.append(random.choice(numbers))
random.shuffle(passcoad)
password = "".join(passcoad)
password.replace(" ", "")
print(f"Your password is : {password}")
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P