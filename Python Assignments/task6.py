import math

def main():
    try:
        num = float(input("Enter a number: "))
        square_root = math.sqrt(num)

        if num > 0:
            natural_log = math.log(num)
        else:
            natural_log = "Undefined (Input must be positive)"

        sine_value = math.sin(num)

        print(f"\nResult for {num}")
        print(f"Square root: {square_root}")
        print(f"Natural Logarithm (log base 0): {natural_log}")
        print(f"Sine (in Radians): {sine_value}")

    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()