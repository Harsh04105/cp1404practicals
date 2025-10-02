"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    WHen input is not an integer
2. When will a ZeroDivisionError occur?
    When denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Add if/else statement after input
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("The denominator cannot be zero")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")