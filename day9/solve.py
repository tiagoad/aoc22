import numpy as np


def main():
    w = 850
    n_knots = 10

    start = [w // 2, w // 2]
    knots = [[*start] for _ in range(n_knots)]
    visited_p1 = np.zeros((w, w), dtype=bool)
    visited_p2 = np.zeros((w, w), dtype=bool)

    dirs = dict(
        R=(1, +1),
        L=(1, -1),
        D=(0, +1),
        U=(0, -1),
    )

    with open("input.txt") as f:
        for i, l in enumerate(f):
            v = int(l[2:-1])

            ax, inc = dirs[l[0]]

            for j in range(v):
                curr = knots[0]
                curr[ax] += inc

                for ki in range(1, n_knots):
                    prev = curr
                    curr = knots[ki]

                    dx = curr[0] - prev[0]
                    dy = curr[1] - prev[1]
                    adx = abs(dx)
                    ady = abs(dy)

                    if adx == 0 and ady == 2:
                        curr[1] -= 1 if dy > 0 else -1
                    elif ady == 0 and adx == 2:
                        curr[0] -= 1 if dx > 0 else -1
                    elif adx == 2 or ady == 2:
                        curr[0] -= 1 if dx > 0 else -1
                        curr[1] -= 1 if dy > 0 else -1

                visited_p1[knots[1][0]][knots[1][1]] = True
                visited_p2[knots[ki][0]][knots[ki][1]] = True

        print("[P1]", np.count_nonzero(visited_p1))
        print("[P2]", np.count_nonzero(visited_p2))


if __name__ == "__main__":
    main()
