import string
import secrets

def generate_password():
    # Phase 1: Input Validation
    while True:
        try:
            length = int(input("Enter desired password length (e.g., 15): "))
            if length < 1:
                print("Length must be at least 1. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Phase 2: Processing and Transformation Engine
    char_pool = string.ascii_letters + string.digits + string.punctuation
    password_list = [secrets.choice(char_pool) for _ in range(length)]
    secure_password = ''.join(password_list)

    # Phase 3: Output
    print("\n--- Password Generated ---")
    print(secure_password)

if __name__ == "__main__":
    generate_password()