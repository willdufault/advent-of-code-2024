data = [...]

safe_cnt = 0
for rep in data:
    for skip in range(len(rep)):
        damp = rep[:skip] + rep[skip + 1 :]
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
