# Q1. Ask user for name, open a file and save input to it
name = input("What is your name? ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# Q2. Open a file and print all content
in_file = open("name.txt")
text = in_file.read()
in_file.close()
print(f"Hi {text}")

# Q3. Open a file and use its desired lines for .....
with open("numbers.txt") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# Q4. OPen a file and use the content inside from each line
total = 0
with open("numbers.txt") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
