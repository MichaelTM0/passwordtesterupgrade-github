# Password Tester (Upgrade)

A command-line Python tool that brute-forces a password up to a user-chosen maximum length, then reports whether it was found, how many attempts it took, and how long it ran. It's an upgraded version of a basic brute-force cracker, restructured into functions with input validation and a clear found / not-found result.

> **Note:** This is an educational tool. It brute-forces a password you enter yourself, on your own machine, to demonstrate how guessing time grows with length. It does not target accounts, systems, or anyone else's data.

## ⚠️ Disclaimer — Educational Use Only

This project was built for **learning purposes** as part of my journey studying
Python and cybersecurity fundamentals. It runs entirely **locally** on a password
the user enters themselves, and it does **not** target, access, or attempt to
compromise any real account, system, or network.

It is intended to demonstrate core programming concepts (loops, `itertools`,
input validation, efficiency) and to illustrate *why* password length and
complexity matter. Please do not use it for anything other than education on
systems you own.

## Features

- Brute-forces a password using a 50-character set (lowercase letters, digits, and common symbols)
- Lets you set the maximum password length to search, and validates that input
- Reports whether the password was found, the number of attempts, and the runtime
- Skips impossible searches instantly (password longer than the max, or using characters outside the set)

## Requirements

- Python 3.6 or newer
- No external packages; it uses only the built-in `itertools` and `time` modules

## Getting Started

1. Clone the repository (update the URL with your GitLab username):

   ```bash
   git clone https://gitlab.com/<your-username>/password-tester-upgrade.git
   cd password-tester-upgrade
   ```

2. Run the program:

   ```bash
   python passwordtesterupgrade.py
   ```

3. Enter a short password and a small maximum length (try 2-3) to start. Longer searches grow very quickly.

## Example

```
Enter your password: ab
What is the maximum password length? 3

Password found: 'ab'
Attempts: 52
Runtime: 0.0000 seconds
```

If the password can't be found within the limit:

```
Enter your password: Zz
What is the maximum password length? 2

Password not found (too long, or it uses characters outside the set).
Attempts: 0
Runtime: 0.0000 seconds
```

## How It Works

- `crack_password()` generates every combination up to the maximum length using `itertools.product`, checking and discarding one guess at a time so only one is ever in memory. It returns a `found` flag, the attempt count, and the runtime, but prints nothing itself.
- `get_max_length()` keeps asking until it gets a valid positive whole number, so a bad entry never crashes the program.
- `show_results()` takes the results and prints either a "found" or "not found" message, followed by the stats.
- Two upfront guards return "not found" instantly when the password is longer than the maximum or contains a character outside the set.

## Why Length Matters

Every character added multiplies the number of possible passwords by the size of the character set (50 here): 50, then 2,500, then 125,000, then 6,250,000, and so on. A short password cracks instantly; a longer one quickly becomes impractical to brute-force. That growth is exactly why length and variety make passwords strong.

## Warning

Do not enter a real password you use anywhere. This is a demonstration tool; use a throwaway test value.

## Future Improvements

- Estimate crack time without running the full search
- Try a list of common passwords first (a dictionary attack)
- Add uppercase letters and more symbols to the set
- Show progress while a long search runs

## What I Learned

- Reusing `itertools.product` and generate-check-discard to avoid running out of memory
- Returning a result (including a found/not-found flag) instead of printing inside the function
- Separating the function that computes from the function that displays
- Validating numeric input with `try/except` so bad input doesn't crash the program
- Avoiding names that shadow Python built-ins (like `eval`)

## Author

**Michael Murchie**

- GitLab: https://gitlab.com/<your-username>
- LinkedIn: [michael-murchie](https://www.linkedin.com/in/michael-murchie/)
