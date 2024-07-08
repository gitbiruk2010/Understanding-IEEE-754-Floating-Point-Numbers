# Calculate positive infinity by multiplying a large number by itself
positive_infinity = 1e308 * 1e308
# Calculate negative infinity by multiplying a large number by itself
negative_infinity = -1e308 * 1e308

# Calculate a NaN value by subtracting positive infinity from itself
nan_value = positive_infinity - positive_infinity

# Check if positive_infinity is equal to float('inf')
is_pos_inf = positive_infinity == float('inf')
print(f"is positive_infinity equal to float('inf)? {is_pos_inf}")

# Check if negative_infinity is equal to float('-inf')
is_neg_inf = negative_infinity == float('-inf')
print(f"is negative_infinity equal to float('-inf)? {is_neg_inf}")

# Check if nan_value is not equal to itself (which is a property of NaN)
is_nan = nan_value != nan_value
print(f"is nan_value not equal to itself? {is_nan}")

# Print the calculated values
print(f"positive inf: {positive_infinity}")
print(f"negative inf: {negative_infinity}")
print(f"nan value: {nan_value}")
