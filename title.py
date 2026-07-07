#Take a string " hello world ". Strip it, convert to title case, and check if it starts with "Hello".
string = "hello world"
result = string.strip().title().startswith("Hello")
print(result)