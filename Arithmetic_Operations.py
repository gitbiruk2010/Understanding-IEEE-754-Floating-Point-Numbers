# arithmetic Operations
from decimal import Decimal

# Define two Decimal numbers
num1 = Decimal('0.1')
num2 = Decimal('0.2')

# Perform addition using standard floating point arithmetic
float_result = 0.1 + 0.2
# Perform addition using Decimal for more accurate arithmetic
decimal_result = num1 + num2

print("Using standard floating point arithmetic:")
print(f"0.1 + 0.2 = {float_result}")
print("Using Decimal for more accurate arithmetic:")
print(f"Decimal('0.1') + Decimal('0.2') = {decimal_result}")

# Perform division using standard floating point arithmetic
float_division_result = 1.0 / 3.0
# Perform division using Decimal for more accurate arithmetic
decimal_division_result = Decimal('1.0') / Decimal('3.0')

print("\nUsing standard floating point arithmetic:")
print(f"1.0 / 3.0 = {float_division_result}")
print("Using Decimal for more accurate arithmetic:")
print(f"Decimal('1.0') / Decimal('3.0') = {decimal_division_result}")
