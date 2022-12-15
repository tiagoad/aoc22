import numpy as np


def get_map():
    m = []

    with open("input.txt") as f:
        for l in f:
            m.append(list(map(int, l[:-1])))

    return np.array(m)


def find_visibility(m):
    w = m.shape[0]
    vis = np.zeros(m.shape)

    side_max_value = np.zeros((4,))

    # the map is square, so we can easily sweep from all sides
    # in the same loop. these functions convert the a and b to
    # coordinates of each directional sweep.
    side_coord_get = [
        # left -> right
        lambda m, a, b: (a, b),
        # right -> left
        lambda m, a, b: (w - a - 1, w - b - 1),
        # top -> down
        lambda m, a, b: (b, a),
        # down -> top
        lambda m, a, b: (w - b - 1, w - a - 1),
    ]

    for a in range(w):
        side_max_value.fill(-1)

        for b in range(w):
            for si, sfn in enumerate(side_coord_get):
                x, y = sfn(m, a, b)
                val = m[x, y]
                if val > side_max_value[si]:
                    vis[x, y] += 1
                    side_max_value[si] = val

    return vis


def main():
    m = get_map()
    v = find_visibility(m)
    print(np.count_nonzero(v))


if __name__ == "__main__":
    main()
