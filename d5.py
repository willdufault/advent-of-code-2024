data = """\
..."""

# Transform data.
from collections import defaultdict

lines = data.split("\n")
mid = lines.index("")
after = defaultdict(set)
for idx in range(mid):
    x, y = lines[idx].split("|")
    after[int(x)].add(int(y))

pages = []
for idx in range(mid + 1, len(lines)):
    page = []
    for num in lines[idx].split(","):
        page.append(int(num))
    pages.append(page)


# Part 1.
def valid(page: list[int]) -> bool:
    seen = set()
    for x in page:
        for y in after[x]:
            if y in seen:
                return False
        seen.add(x)
    return True


total = 0
for page in pages:
    if valid(page):
        total += page[len(page) // 2]
print(total)

# Part 2
from functools import cache


@cache
def count(x: int) -> int:
    cnt = 0
    for y in after[x]:
        if y in page_set:
            cnt = max(cnt, 1 + count(y))
    return cnt


total = 0
for page in pages:
    if not valid(page):
        page_set = set(page)
        pairs = []
        for num in page:
            pairs.append((count(num), num))
        pairs.sort()
        total += pairs[len(page) // 2][1]
        count.cache_clear()
print(total)
