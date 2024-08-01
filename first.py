# Write a program to emulate a calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("======================================================")
print("--- Enter the symbol for the arithmetic calculation ---")
print("Enter (+) for addition...")
print("Enter (-) for subtraction...")
print("Enter (*) for multiplication...")
print("Enter (/) for division...")
print("==============================")
symbol = input("Enter the desired symbol: ")

dictionary = {"+": num1 + num2, "-": num2 - num2, "/": num1 / num2, "*": num1 * num2}
if symbol == "+" or "-" or "*" or "/":
    operation = dictionary.get(symbol)
    print(f"The result of the operation ({symbol}) on {num1} and {num2} is:", operation)
else:
    print("Please enter a valid symbol!")
