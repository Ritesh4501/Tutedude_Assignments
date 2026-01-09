def main():
    total_sum = 0

    # 1. Uses a for loop to iterate over numbers from 1 to 50
    # Note: range(1, 51) includes 1 and stops at 50
    for i in range(1,51):
        total_sum += i  # 2. Calculates the sum of all integers in this range
    
    # 3. Displays the final sum
    print(f"The sum of the numbers from 1 to 50 is: {total_sum}")

if __name__ == "__main__":
    main()
