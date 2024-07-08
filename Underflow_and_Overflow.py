from decimal import Decimal, getcontext, Overflow, Underflow

# Function to demonstrate underflow in decimal calculations
def demonstrate_underflow():
    # Set the precision of the decimal context to 5
    getcontext().prec = 5
    
    try:
        # Define a very small number
        small_number = Decimal('1e-20')
        # Multiply the small number by itself
        result = small_number * small_number
        print(f"Underflow Result: {result}")
    except Underflow:
        # Catch and handle underflow exception
        print("Underflow occurred")

# Function to demonstrate overflow in decimal calculations
def demonstrate_overflow():
    # Set the precision of the decimal context to 50
    getcontext().prec = 50
    
    try:
        # Define a very large number
        large_number = Decimal('1e+20')
        # Raise the large number to the power of 20
        result = large_number ** 20
        print(f"Overflow Result: {result}")
    except Overflow:
        # Catch and handle overflow exception
        print("Overflow occurred")

# Demonstrate underflow
print("Demonstrating Underflow:")
demonstrate_underflow()

# Demonstrate overflow
print("\nDemonstrating Overflow:")
demonstrate_overflow()
