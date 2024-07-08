# Pythonto demo IEEE 754 handling

import math
from decimal import Decimal, getcontext, Overflow, Underflow, InvalidOperation

# Setting up the decimal context
context = getcontext()
context.prec = 34  # Precision
context.rounding = "ROUND_HALF_EVEN"  # Default rounding mode

def demonstrate_ieee754_python():
    # Demo rounding
    rounded_value = Decimal('1.2345678901234567890123456789012345').quantize(Decimal('1.234567890123456789012345678901234'))
    print(f"Rounded value in Python: {rounded_value}")

    # Demo overflow
    try:
        result = Decimal('1e1000') * Decimal('1e1000')
    except Overflow:
        print("Overflow occurred in Python")

    # Demo underflow
    try:
        result = Decimal('1e-1000') * Decimal('1e-1000')
    except Underflow:
        print("Underflow occurred in Python")

    # Demo invalid operation
    try:
        result = Decimal('0') / Decimal('0')
    except InvalidOperation:
        print("Invalid operation in Python")

demonstrate_ieee754_python()
