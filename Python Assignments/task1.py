def main():
    print("--- Basic Mathematical Operations ---")
    
    try:
        # 1. Takes two numbers as input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # 2. Performs mathematical operations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        
        # Handling division by zero
        if num2 != 0:
            division = num1 / num2
            print(f"Division: {division:.2f}")
        else:
            division = "Undefined (cannot divide by zero)"

        # 3. Displays the results
        print("\nResults:")
        print(f"Addition: {num1} + {num2} = {addition}")
        print(f"Subtraction: {num1} - {num2} = {subtraction}")
        print(f"Multiplication: {num1} * {num2} = {multiplication}")
        print(f"Division: {num1} / {num2} = {division}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()