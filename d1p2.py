left = [...]
right = [...]

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
