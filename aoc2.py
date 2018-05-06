def aoc2_a(input):
    rows = input.split("\n")
    checksum = 0
    for row in rows:
        items = list(map(int, row.split("\t")))
        min_item = min(items)
        max_item = max(items)
        checksum += max_item - min_item

    return checksum
