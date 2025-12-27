def is_narcissistic(n):
    # 1. Convert to string to find the number of digits (the power)
    power = len(str(n))
    
    # 2. Use a temporary variable for the loop so we don't destroy 'n'
    temp = n
    total_sum = 0
    
    # 3. Use 'temp' for BOTH the condition and the digit extraction
    while temp > 0:
        digit = temp % 10             # Get last digit
        total_sum += (digit ** power) # Add digit to the power of total digits
        temp //= 10                   # Remove last digit
        
    # 4. Compare the result with the original number
    if total_sum == n:
        print(f"{n} is a Narcissistic Number! ✨")
    else:
        print(f"{n} is not a Narcissistic Number. (Sum was {total_sum})")

# --- Get User Input ---
try:
    user_num = int(input("Enter a 4-digit number: "))
    
    # Optional: Check if it's actually 4 digits
    if 1000 <= user_num <= 9999:
        is_narcissistic(user_num)
    else:
        print("Please ensure you enter exactly 4 digits.")
except ValueError:
    print("Invalid input. Please enter a whole number.")