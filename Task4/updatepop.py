# Create a dictionary. Add 3 items using update(), then remove the last inserted item using popitem().

d = { }
d.update({"a": 1, "b": 2})
d.update({"c":3 ,"d":4})
d.update({"e":5,"f":6})
print(d.pop("f"))