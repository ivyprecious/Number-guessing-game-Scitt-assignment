# Initialize previous number
previous_number = 0

# Loop through numbers from 1 to 10
for current_number in range(1, 11):
    # Calculate the sum
    total = previous_number + current_number
    print(f"Current Number: {current_number}, Previous Number: {previous_number}, Sum: {total}")
    
    # Update previous_number for the next iteration
    previous_number = current_number
