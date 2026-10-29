# Sum of digits
number = int(input("Enter a number: "))
if number < 0:
    number = -number
total = 0
while number > 0:
    digit = number % 10      
    total = total + digit    
    number = number // 10    
print("The sum of the digits is:", total)