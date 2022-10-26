print("Welcome to the tip calculatir.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill?"))
billTip = bill * (1 + tip/100)
pay = billTip / split
print("Each person should pay: $",round(pay,2))