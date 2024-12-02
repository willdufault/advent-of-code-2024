data = """\
..."""

# Transform data.
reports = []
for line in data.split("\n"):
    report = []
    for num in line.split():
        report.append(int(num))
    reports.append(report)

# Part 1.
safe_cnt = 0
for report in reports:
    inc = report[1] > report[0]
    prv = report[0]
    for lvl in report[1:]:
        diff = abs(lvl - prv)
        if diff < 1 or diff > 3 or (lvl > prv) != inc:
            break
        prv = lvl
    else:
        safe_cnt += 1
print(safe_cnt)

# Part 2.
safe_cnt = 0
for report in reports:
    if len(report) == 2:
        safe_cnt += 1
        continue

    for idx in range(len(report)):
        damp = report[:idx] + report[idx + 1 :]
        inc = damp[1] > damp[0]
        prv = damp[0]
        for lvl in damp[1:]:
            diff = abs(lvl - prv)
            if diff < 1 or diff > 3 or (lvl > prv) != inc:
                break
            prv = lvl
        else:
            safe_cnt += 1
            break
print(safe_cnt)
