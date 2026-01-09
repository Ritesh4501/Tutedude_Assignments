def main():
    # 1. Takes an integer input from the user
    try:
        user_input = input("Enter a number:- ")
        number = int(user_input)

        # 2. By using if-else statemnet it will check whether the input number is even or odd
        if number % 2 == 0:
            # 3. Diplaying the output according to the result
            print(f"{number} is an Even number.")
        else:
            print(f"{number} is an Odd number.")

    except ValueError:
        print("Invalid input!!! Please Enter a whole integer.")

if __name__ == "__main__":
    main()