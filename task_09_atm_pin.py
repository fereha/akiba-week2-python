correct_pin = 1234
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    pin = int(input("Enter your PIN: "))
    attempts = attempts + 1

    if pin == correct_pin:
        print("PIN correct. Access granted.")
        break
    else:
        remaining = max_attempts - attempts
        print("Incorrect PIN.")
        print("Attempts remaining:", remaining)

if pin != correct_pin:
    print("Too many wrong attempts. Your card is blocked.")