#Question 7: 
#Python 
# Take a word from user. 
# Check if the word is a palindrome or not. 
# (Example: "madam", "radar") 

text = "madam"

reversed_text = text[::-1]
if text == reversed_text:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")    



