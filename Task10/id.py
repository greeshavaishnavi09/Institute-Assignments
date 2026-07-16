# Explain what id(5) does. Why do two variables with the same value sometimes have the same id() 
# and sometimes different?

a = 15
print(id(a))

a1 = 12
a2 = 12
print(id(a1))
print(id(a2))

