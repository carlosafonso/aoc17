def aoc2_a(input):
    rows = input.split("\n")
    checksum = 0
    for row in rows:
        items = list(map(int, row.split("\t")))
        min_item = min(items)
        max_item = max(items)
        checksum += max_item - min_item

    return checksum


def aoc2_b(input):
    rows = input.split("\n")
    checksum = 0
    for row in rows:
        items = list(map(int, row.split("\t")))
        done = False
        for k, i in enumerate(items):
            for j in items[k + 1:]:
                if i > j and i % j == 0:
                    checksum += int(i / j)
                    done = True
                    break
                if i < j and j % i == 0:
                    checksum += int(j / i)
                    done = True
                    break
            if done:
                break

    return checksum
