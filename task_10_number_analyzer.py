total = 0
even_count = 0
odd_count = 0
largest = 0
smallest = 0

for i in range(1, 11):
    number = int(input("Enter number " + str(i) + ": "))

    total = total + number

    if i == 1:
        largest = number
        smallest = number
    else:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    if number % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

average = total / 10

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Total sum:", total)
print("Average:", average)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)