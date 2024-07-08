from decimal import Decimal, getcontext, ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR

# Function to demonstrate rounding in different modes
def rounding_example(value):
    # Get the current decimal context
    context = getcontext()
     
    # Define the different rounding modes
    rounding_modes = {
        "ROUND_CEILING": ROUND_CEILING,
        "ROUND_DOWN": ROUND_DOWN,
        "ROUND_FLOOR": ROUND_FLOOR 
    }
    
    # Dictionary to store the results for each rounding mode
    results = {}
    
    # Apply each rounding mode and store the result
    for name, mode in rounding_modes.items():
        context.rounding = mode
        rounded_value = value.quantize(Decimal('1.'), context=context)
        results[name] = rounded_value
    
    return results

# Define the value to be rounded
value = Decimal('2.5')
# Get the rounded results for the value
rounded_results = rounding_example(value)

# Print the results for each rounding mode
for mode, result in rounded_results.items():
    print(f"{mode}: {result}")

# Define a new value to be rounded
value = Decimal('2.45')

# Get the rounded results for the new value
rounded_results = rounding_example(value)

print("\nFor the value 2.45:")
# Print the results for each rounding mode
for mode, result in rounded_results.items():
    print(f"{mode}: {result}")
