import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
next = True
allbids= {}
def bidder(bid):
  highest = 0
  for b in bid:
    bide = bid[b]
    if bide > highest:
      highest = bide
      key = b
  print(f"The winner is {key} with a bid of ${highest}.")
while(next):
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  allbids[name] = bid
  choice = input("Are ther any other bidders? Type 'yes' or 'no'. ")
  if choice == 'no':
    next = False
    bidder(allbids)
   #maxName = max(allbids.keys())
    #maximum = max(allbids.values())
    #print(f"The winner is {maxName} with a bid of {maximum}")
  elif choice == 'yes':
     os.system('clear')