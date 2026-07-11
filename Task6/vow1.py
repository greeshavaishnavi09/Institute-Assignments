# Take a character and check if it is a vowel (a, e, i, o, u) or consonant.

char = input("enter a name:")
vow = ("a","e","i","o","u")
if char in vow :
    print("vowel")
elif char.isalpha():
    print("consonant")
else:
    print("none")