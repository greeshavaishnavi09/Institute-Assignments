#Take a sentence. Split into words, remove all words that start with vowel (a,e,i,o,u), then join remaining words.

text = "python is a prog language"
words = text.split()
vow= "aeiou"
fil_words = [word for word in words if not word[0] in vow]
print(f"{" ".join(fil_words)}")