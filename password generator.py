import random
import string

def password_generator():
    print("-----------------------------------")
    print("      PYTHON PASSWORD GENERATOR    ")
    print("-----------------------------------")
    
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length must be greater than zero.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    print("\nSelect Complexity Level:")
    print("1. Letters only (Low)")
    print("2. Letters and Numbers (Medium)")
    print("3. Letters, Numbers, and Symbols (High)")
    
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        characters = string.ascii_letters
    elif choice == '2':
        characters = string.ascii_letters + string.digits
    elif choice == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice! Defaulting to High complexity.")
        characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    password_generator()