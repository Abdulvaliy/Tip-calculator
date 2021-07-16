#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6

print("Welcometo the tip calculator.")
bill = float(input("What was the total bill? $"))

percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

people = int(input("How many people to split the bill? "))

cost = str(round((bill * (100 + percent)/100) / people , 2))
print(f"Each person should pay: ${cost}")

