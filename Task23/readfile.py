file= open("data.txt","r")
print(file.read())

file =open("information.txt","w") 
file.write("hi,\n hello,greesha,how r u ,\n bye")
print(file.close())

file =open("information.txt","r") 
print(file.read())

with open("information.txt","r+") as file:
    file.read()
    file.write("vaishnavi")
    print(file.r+())
