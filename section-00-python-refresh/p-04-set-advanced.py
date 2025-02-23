friends = {"Bob", "Mary", "Peter"}
abroad = {"Bob", "Peter"}

# difference: returns elements in friends that are not in abroad
local_friends = friends.difference(abroad)
print(f"Local friends: {local_friends}")

# union: returns all elements in both sets
tight_ends = {"Gronk"}
wide_receivers = {"Edelman", "Brown"}
all_receivers = tight_ends.union(wide_receivers)
print(f"All receivers: {all_receivers}")

# intersection: returns elements in both sets
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print(f"Both art and science: {both}")
