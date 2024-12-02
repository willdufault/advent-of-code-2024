data = """\
..."""

left = []
right = []
for line in data.split("\n"):
    loc1, loc2 = line.split()
    left.append(int(loc1))
    right.append(int(loc2))

# Part 1.
# Time: O(nlogn)
# Space: O(n)
left.sort()
right.sort()

dist = 0
for loc1, loc2 in zip(left, right):
    dist += abs(loc1 - loc2)
print(dist)

# Part 2.
# Time: O(n)
# Space: O(n)
freq = {}
for loc in left:
    freq[loc] = 0
for loc in right:
    if loc in freq:
        freq[loc] += 1

sim_score = 0
for loc, cnt in freq.items():
    sim_score += loc * cnt
print(sim_score)
