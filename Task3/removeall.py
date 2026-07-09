#Given data = [10, 20, 30, 20, 40, 20], remove all occurrences of 20 (use loop or multiple remove).

data= [10, 20, 30, 20, 40, 20]
while 20 in data:
    data.remove(20)
print(data)