#Take a sentence and replace the word "bad" with "good" after splitting and joining.

text = "It's a very bad product"
print(f"{"_".join(text.split()).replace("bad","good")}")