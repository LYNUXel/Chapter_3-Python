# Creating an empty set
s=set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

print("The elements from the set are: ")
print(s)
s.add(3)

s.remove(3)
s.add(5)
print("Added element 5 and removed element 3 now the elements from the set are: ")
print(s)

print(f"Now, the set has {len(s)} elements left.")