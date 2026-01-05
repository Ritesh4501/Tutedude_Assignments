def main():
    print("--- Personalized Greeting ---")
    
    # 1. Takes user's first and last name as input
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    # 2. Concatenates the first name and last name
    full_name = first_name + " " + last_name

    # 3. Prints a personalized greeting message
    if full_name.strip():
        print(f"\nHello, {full_name}! Welcome to the Python Course.")
    else:
        print("\nHello! It looks like you didn't enter a name.")

if __name__ == "__main__":
    main()