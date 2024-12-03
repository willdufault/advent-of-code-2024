data = """\
..."""

# Part 1.
from re import findall

total = 0
pattern = r"mul\(\d+,\d+\)"
matches = findall(pattern, data)
for match in matches:
    a, b = match.strip("mul()").split(",")
    total += int(a) * int(b)
print(total)

# Part 2.
total = 0
pattern = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
matches = findall(pattern, data)
enabled = True
for match in matches:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    elif enabled:
        a, b = match.strip("mul()").split(",")
        total += int(a) * int(b)
print(total)
