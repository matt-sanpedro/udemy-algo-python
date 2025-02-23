# LIST
l = ["Bob", "Mary", "Peter"]
l.remove("Bob")

# TUPLE
# similar to list but immutable (cannot modify)
t = ("Bob", "Mary", "Peter")
# t[0] = "Sarah" # this will raise an error because tuples are immutable

# SET
# can add or remove elements, but is unordered and cannot have duplicates
s = {"Bob", "Mary", "Peter"}
# print(s[0]) # this will raise an error because sets are unordered
s.add("Smith")
s.add("Smith") # this will not add a duplicate - will be ignored
