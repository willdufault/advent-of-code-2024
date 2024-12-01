left = [...]
right = [...]

left.sort()
right.sort()

dist = 0
for loc1, loc2 in zip(left, right):
    dist += abs(loc1 - loc2)
print(dist)
