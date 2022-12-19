import numpy as np

W = 500
H = 172
OFFSET_X = 250
OFFSET_Y = 0
SOURCE_X = 500


def main():
    m, max_y = get_map()

    steps_p1 = simulate(m.copy())
    print(f"[P1] {steps_p1}")

    draw_line(m, 0, max_y + 2, W - 1, max_y + 2)
    steps_p2 = simulate(m.copy())
    print(f"[P2] {steps_p2}")


def simulate(m):
    it = 0
    while add_sand(m, *offset(SOURCE_X, 0)):
        it += 1
        # print(f"== {it} ==")
        # print_map(m)
        # print()
    return it


def add_sand(m, x, y):
    if m[y, x] == "o":
        return False

    m[y, x] = "+"

    try:
        while True:
            if m[y + 1, x] == ".":
                y, x = y + 1, x

            elif x > 0 and m[y + 1, x - 1] == ".":
                y, x = y + 1, x - 1

            elif x < W - 1 and m[y + 1, x + 1] == ".":
                y, x = y + 1, x + 1

            else:
                m[y, x] = "o"
                return True

    except IndexError:
        # if not final:
        #    add_sand(m, orig_x, orig_y, final=True)
        return False


def offset(x, y):
    x, y = x - OFFSET_X, y - OFFSET_Y
    if x < 0 or y < 0:
        raise ValueError(f"Invalid coordinates: ({x}, {y})")
    else:
        return x, y


def draw_line(m, x1, y1, x2, y2):
    # print(f"{x1}, {y1} -> {x2}, {y2}")

    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1

        m[y1 : y2 + 1, x1] = "#"
    else:
        if x1 > x2:
            x1, x2 = x2, x1

        m[y1, x1 : x2 + 1] = "#"


def get_map():
    m = np.full((H, W), ".")
    max_y = 0

    with open("input.txt") as f:
        for l in f:
            steps = map(lambda el: map(int, el.split(",")), l[:-1].split(" -> "))
            x1, y1 = next(steps)
            for x2, y2 in steps:
                draw_line(m, *offset(x1, y1), *offset(x2, y2))

                if y2 > max_y:
                    max_y = y2

                x1, y1 = x2, y2

    return m, max_y


def print_map(m):
    for l in m:
        for c in l:
            print(end=c)
        print()
    print()


if __name__ == "__main__":
    main()
