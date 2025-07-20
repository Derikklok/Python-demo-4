# AREPL compatibility - hardcode input for testing
standard_input = '1'  # Change this value to test different options (1, 2, 3, or 4)

def get_user_input():
    """Get user input with proper error handling"""
    try:
        if 'standard_input' in globals():
            # For AREPL - use hardcoded input
            user_input = standard_input
            print(f"Enter option : {user_input}")
        else:
            # For normal execution - get user input
            user_input = input("Enter option : ")
        
        if user_input.strip() == "":
            print("Error: No input provided!")
            return None
            
        return int(user_input)
    except ValueError:
        print(f"Error: '{user_input}' is not a valid number!")
        return None

def getSum(a, b):
    """Calculate sum of two numbers"""
    total = a + b
    return total

def getDiscount(total_price, limit):
    """Calculate discount amount"""
    discount = total_price - limit
    return discount

def main():
    """Main program function"""
    print("=== Python Calculator ===")
    print("1. Calculate Sum (5 + 10)")
    print("2. Calculate Discount (20 - 10)")
    print("3. Option 3 (Coming Soon)")
    print("4. Exit")
    print("=" * 25)
    
    user_option = get_user_input()
    
    if user_option is None:
        return
    
    match user_option:
        case 1:
            result = getSum(5, 10)
            print(f"Total is: {result}")
        case 2:
            result = getDiscount(20, 10)
            print(f"Final price is: {result}")
        case 3:
            print("Option 3 - Feature coming soon!")
        case 4:
            print("Goodbye!")
        case _:
            print("Error: Please enter a number between 1-4")

# Run the program
if __name__ == "__main__":
    main()
        
