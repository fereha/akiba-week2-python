# Largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a == b and b == c:
    print("All three numbers are equal.")
elif a >= b and a >= c:
    if a == b or a == c:
        print(a, "is the largest (it appears more than once).")
    else:
        print(a, "is the largest.")
elif b >= a and b >= c:
    if b == a or b == c:
        print(b, "is the largest (it appears more than once).")
    else:
        print(b, "is the largest.")
else:
    print(c, "is the largest.")