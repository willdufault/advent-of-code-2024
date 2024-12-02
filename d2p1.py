data = [...]

safe_cnt = 0
for rep in data:
    inc = rep[1] > rep[0]
    prv = rep[0]
    for lvl in rep[1:]:
        diff = abs(lvl - prv)
        if diff < 1 or diff > 3 or (lvl > prv) != inc:
            break
        prv = lvl
    else:
        safe_cnt += 1
print(safe_cnt)
