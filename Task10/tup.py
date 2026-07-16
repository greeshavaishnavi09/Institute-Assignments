# Advanced Enumeration + Zip + Condition You have two lists:
# names = ["Sumit", "Rahul", "Priya", "Aman", "Neha"]
# scores = [85, 92, 78, 95, 88]
# Write a single list comprehension using enumerate() and zip() that returns a list of tuples in this format: [(index, name, "Excellent")] if score ≥ 90, else [(index, name,"Good")]

names = ["Sumit", "Rahul", "Priya", "Aman", "Neha"]
scores = [85, 92, 78, 95, 88]

result = [(i , names ,"Excellent" if scores>=90 else "Good") for i ,(names,scores) in enumerate(zip(names,scores))]

print(result)