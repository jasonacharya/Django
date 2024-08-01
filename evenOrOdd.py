try:
    num = float(input("Enter the number: "))
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
except:
    print("Please enter a valid number!")
