#import the necessary library
import struct

# Function to convert a float to its IEEE 754 binary string representation
def float_to_ieee_754(n):
    # Pack the float as a 4-byte binary data in big-endian format
    packed = struct.pack('>f', n)
    # Convert the packed bytes to an integer
    packed_int = int.from_bytes(packed, byteorder='big')
    # Format the integer as a 32-bit binary string
    binary_str = f'{packed_int:032b}'
    return binary_str

# Function to test the IEEE 754 conversion for normal and edge cases
def test_ieee_754_conversion():
    # List of normal numbers to test
    numbers = [0.15625, -4.75, 3.14159265359]
    # List of edge cases to test
    edge_cases = [0.0, -0.0, float('inf'), float('-inf'), float('nan')]
    
    print("Normal Cases:")
    # Convert and print the IEEE 754 representation for normal numbers
    for num in numbers:
        print(f"Decimal: {num} -> IEEE 754: {float_to_ieee_754(num)}")

    print("\nEdge Cases:")
    # Convert and print the IEEE 754 representation for edge cases
    for case in edge_cases:
        print(f"Decimal: {case} -> IEEE 754: {float_to_ieee_754(case)}")

# Run the test function to display results
test_ieee_754_conversion()
