import numpy as np
import collections


def get_map():
    m = []
    with open("input.txt") as f:
        start = None
        end = None

        for y, l in enumerate(f):
            row = []
            for x, c in enumerate(l[:-1]):
                if c == "S":
                    start = (x, y)
                    c = "a"
                elif c == "E":
                    end = (x, y)
                    c = "z"

                row.append(ord(c) - ord("a"))
            m.append(row)

    return np.array(m), start, end


# dijkstra's algo
def solve(m, start, end):
    queue = collections.deque([[start]])
    seen = {start}

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        v = m[y][x]
        if (x, y) == end:
            return path

        for x2, y2 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (x2, y2) in seen:
                continue

            try:
                v2 = m[y2][x2]
            except IndexError:
                continue

            if (v2 - v) <= 1:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


def main():
    m, start, end = get_map()
    path = solve(m, start, end)

    print(f"[P1] {len(path)-1}")


if __name__ == "__main__":
    main()
