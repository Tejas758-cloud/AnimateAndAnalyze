print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would like to give? 10 12 15"))
people = int(input("How many people to split the bill?"))
total = (bill + bill * tip / 100) / people
print(f"Each person should pay: ${total:.2f}")



