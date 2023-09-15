try:
    num = input("Enter a number: ")
    num = int(num)
except ValueError:
    print("An incorrect value was passed to int()")
