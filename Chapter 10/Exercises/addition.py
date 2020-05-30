"""Ask user for two numbers and print the sum of these numbers"""

print("Enter two numbers below and I will add them and show you the result.")
while True:
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        sum = num1 + num2
        print(sum)
        break
    except ValueError:
        print("Please enter only numbers!")
        continue
