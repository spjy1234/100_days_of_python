def add_tip_bill(bill, tip):
    total = bill + (bill * tip / 100)
    return total

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
cost = add_tip_bill(bill, tip)
people = int(input("How many people to split the bill?"))
last_payment = cost / people
print(f"Each person should pay: {round(last_payment, 2)}")