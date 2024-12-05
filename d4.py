data = """\
..."""

# Transform data.
mtx = []
for line in data.split("\n"):
    mtx.append([*line])


# Part 1.
def check(r: int, c: int, dr: int, dc: int, i: int) -> bool:
    if i == len(word):
        return True

    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False

    if mtx[r][c] != word[i]:
        return False

    return check(r + dr, c + dc, dr, dc, i + 1)


rows, cols = len(mtx), len(mtx[0])
word = "XMAS"
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
cnt = 0
for r in range(rows):
    for c in range(cols):
        for dr, dc in dirs:
            if check(r, c, dr, dc, 0):
                cnt += 1
print(cnt)


# Part 2.
cnt = 0
for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        if mtx[r][c] == "A":
            up_left = mtx[r - 1][c - 1]
            up_right = mtx[r - 1][c + 1]
            down_left = mtx[r + 1][c - 1]
            down_right = mtx[r + 1][c + 1]
            diag1 = sorted([up_left, down_right]) == ["M", "S"]
            diag2 = sorted([up_right, down_left]) == ["M", "S"]
            if diag1 and diag2:
                cnt += 1
print(cnt)
