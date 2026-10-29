# Prime number checker
# Step 1: Get the number from the user
number = int(input("Enter a number: "))
# Step 2: Numbers less than 2 are NOT prime
# This covers 0, 1 and all negative numbers
if number < 2:
    print(number, "is not a prime number.")
else:
    # Step 3: Start by assuming the number IS prime
    # (we will change this to False if we find a divisor)
    is_prime = True
    # Step 4: Start testing divisors from 2
    i = 2
    # Keep looping while i * i is not bigger than the number.
    # We stop early because divisors come in pairs.
    # Example: 36 = 2 x 18, 3 x 12, 4 x 9, 6 x 6
    # The smaller number in each pair is never bigger than the square root,
    # so if we find no divisor by then, there is none.
    while i * i <= number:
    # Step 5: Check if i divides the number exactly
        # (remainder 0 means it divides exactly)
        if number % i == 0:
            is_prime = False   # we found a divisor, so it is NOT prime
            break              # stop the loop, we already know the answer
  # Step 6: Move to the next divisor
        i = i + 1
  # Step 7: Show the result
    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")