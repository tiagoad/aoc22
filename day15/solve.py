import re


def compute_line(y, sx, sy, bx, by):
    s_b_taxicab = abs(sx - bx) + abs(sy - by)
    l_s_dy = abs(y - sy)
    b_x0, b_x1 = sx - s_b_taxicab + l_s_dy, sx + s_b_taxicab + 1 - l_s_dy
    if b_x1 - b_x0 > 0:
        return b_x0, b_x1
    else:
        return None


def merge_ranges(ranges):
    merged = []
    for x0, x1 in sorted(ranges):
        if merged and merged[-1][1] >= x0:
            merged[-1] = (merged[-1][0], max(merged[-1][1], x1))
        else:
            merged.append((x0, x1))
    return merged


def compute_y(y, data):
    ranges = []

    for sx, sy, bx, by in data:
        r = compute_line(y=y, sx=sx, sy=sy, bx=bx, by=by)

        if r is not None and r[1] >= r[0]:
            ranges.append(r)

    ranges = merge_ranges(ranges)

    return ranges


def main():
    data = []
    with open("input.txt") as f:
        for l in f:
            m = re.match(
                r"Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)",
                l,
                re.ASCII,
            )
            if m:
                data.append(tuple(map(int, m.groups())))

    r = compute_y(2000000, data)
    if r:
        print(f"[P1] {r[0][1] - r[0][0] - 1}")

    # there's certainly a more efficient solution, but this works well enough
    # for the N. not particularly proud but that's life.
    for y in range(0, 4000000):
        r = compute_y(y, data)
        if len(r) > 1:
            x = r[0][1]
            v = (x * 4000000) + y
            print(f"[P2] {v} ({x}, {y})")
            break



if __name__ == "__main__":
    main()
