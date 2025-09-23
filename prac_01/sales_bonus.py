"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus_percent = 15
        bonus_amount = sales * 0.15
    else:
        bonus_percent = 10
        bonus_amount = sales * 0.10

    print(f"Your Sales ${sales}, Bonus is {bonus_percent}% = ${bonus_amount:.2f}.")
    sales = float(input("Enter sales: $"))

print(f"Wrong input.")
