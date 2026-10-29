## Task 8: Count Numbers

**1. Understand:** The program asks for a positive number N. It must count from 1 to N and find how many numbers are even, how many are odd, and the sum of all of them.

**2. Break it down:**
- Get N from the user.
- Go through every number from 1 to N.
- Decide if each number is even or odd.
- Keep a running total.
- Show the three results.

**3. Patterns:** The same steps repeat for every number: check even or odd, then add to the sum. Even numbers always have no remainder when divided by 2.

**4. Design the logic:**
- Start three counters at 0: `even_count`, `odd_count`, `total`.
- Use one `for` loop from 1 to N.
- Inside the loop, add the number to `total`. Use `if i % 2 == 0` to add 1 to `even_count`, otherwise add 1 to `odd_count`.

**5. Implement:** See the Task 8 code (a single `for` loop with three counters).

**6. Test:**
- Normal: N = 10 → 5 even, 5 odd, sum 55.
- Edge case: N = 1 → 0 even, 1 odd, sum 1.
- Unusual: N = 0 or a negative number → the loop does not run, so you get 0, 0, 0. A check for positive numbers could be added.

**7. Improve:** One loop does all three jobs, so there's no need for three loops. The code could also reject numbers that aren't positive.

---

## Task 9: ATM PIN System

**1. Understand:** The correct PIN is 1234. The user has a maximum of 3 attempts. After each wrong try, show how many attempts remain. After 3 wrong tries, block access.

**2. Break it down:**
- Store the correct PIN and the maximum attempts.
- Ask for the PIN.
- Compare it with the correct PIN.
- Count the attempts.
- Show the attempts remaining.
- Stop the program when the PIN is right or the attempts run out.

**3. Patterns:** Asking, checking, and counting repeats until the PIN is correct or 3 attempts are used.

**4. Design the logic:**
- Use `while attempts < 3`.
- Inside, add 1 to `attempts` each time.
- `if pin == correct_pin` → access granted, then `break`.
- `else` → print `Attempts remaining: 3 - attempts`.
- After the loop, if the PIN was never correct, print the blocked message.

**5. Implement:** See the Task 9 code.

**6. Test:**
- Correct on the first try.
- Wrong twice, correct on the third.
- Wrong three times → blocked.
- Unusual: typing letters causes an error with `int()`. The bank project avoids this by treating the PIN as text.

**7. Improve:** Use a `break` or a flag like `access = True` so the loop stops as soon as the PIN is right. Store the PIN as text so a PIN starting with 0 works.

---

## Task 10: Number Analyzer

**1. Understand:** The user enters 10 numbers. The program shows the largest, smallest, sum, average, and the count of even and odd numbers. It should use one main loop.

**2. Break it down:**
- Read 10 numbers.
- Track the largest and the smallest so far.
- Add each number to a total.
- Count evens and odds.
- After the loop, calculate the average (total ÷ 10).

**3. Patterns:** Every number gets the same four checks: add to the sum, compare with the largest, compare with the smallest, and check even or odd.

**4. Design the logic:**
- Use one `for` loop that repeats 10 times.
- On the first number, set both `largest` and `smallest` to it.
- For the other numbers, update them with `if number > largest` and `if number < smallest`.
- Use `number % 2 == 0` for even or odd.
- Calculate the average after the loop.

**5. Implement:** See the Task 10 code.

**6. Test:**
- Normal: 5, 8, 3, 10, 7, 2, 9, 4, 6, 1 → largest 10, smallest 1, sum 55, average 5.5.
- Edge case: all negative numbers → this is why we set `largest` and `smallest` from the first number instead of 0.
- Edge case: all numbers the same → largest and smallest are equal.
- Edge case: all even or all odd → one count is 0.

**7. Improve:** Everything is done in one loop, which is simpler and faster than several loops. Later, you could learn lists and use `max()`, `min()`, and `sum()`, which make this shorter.

---

If your teacher wants these as a document, I can put them into a Word file or PDF for you. Just tell me which one.
