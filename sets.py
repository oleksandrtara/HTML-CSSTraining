
#Example of sets in Python where if you add additonal value that already in the set, it will keep an original amount of elements

s = set()

#Add elemets to set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(4)

s.remove(2)

print(s)
print(f"There are {len(s)} elements in the set")