data = """\
..."""

left = []
right = []
for line in data.split("\n"):
    loc1, loc2 = line.split()
    left.append(int(loc1))
    right.append(int(loc2))

left.sort()
right.sort()

dist = 0
for loc1, loc2 in zip(left, right):
    dist += abs(loc1 - loc2)
print(dist)
