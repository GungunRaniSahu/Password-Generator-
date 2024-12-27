import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    char_pool = ""
    if use_upper:
        char_pool += upper
    if use_lower:
        char_pool += lower
    if use_digits:
        char_pool += digits
    if use_symbols:
        char_pool += symbols

    if not char_pool:
        raise ValueError("At least one character type must be selected.")

    password = "".join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length (default 12): ") or 12)
    use_upper = input("Include uppercase letters? (y/n, default y): ").lower() in ["y", "yes", ""]
    use_lower = input("Include lowercase letters? (y/n, default y): ").lower() in ["y", "yes", ""]
    use_digits = input("Include digits? (y/n, default y): ").lower() in ["y", "yes", ""]
    use_symbols = input("Include symbols? (y/n, default y): ").lower() in ["y", "yes", ""]

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
