# Even or Odd program
number = int(input("Enter a number: "))
if number == 0:
    print("the number is zero . It is an even number.")
elif number % 2 == 0:
    if number > 0:
        print(number, "is a positive even number.")
    else:
        print(number, "is a negative even number.")
else:
    if number > 0:
        print(number, "is a positive odd number.")
    else:
        print(number, "is a negative odd number.")