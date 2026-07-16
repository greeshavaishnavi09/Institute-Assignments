# 2. Hard Type Conversion + Logical Functions Given this messy list:Python
# data = ["10", "abc", "25.5", "30", "", "45.0", "xyz", "60"]
# Write a list comprehension that:
# Converts valid integers and floats to int type
# Skips non-numeric values
# Uses try-except inside the comprehension (or any() / all())
# Returns only integer values


data = ["10", "abc", "25.5", "30", "", "45.0", "xyz", "60"]
result = [int(float(item)) for item in data if item and all(ch.isdigit() or ch == "." for ch in item)]
print(result)