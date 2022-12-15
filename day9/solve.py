import numpy as np


def main():
    w = 850

    start = [w // 2, w // 2]
    head = start.copy()
    tail = start.copy()
    visited = np.zeros((w, w), dtype=bool)

    dirs = dict(
        R=(1, +1),
        L=(1, -1),
        D=(0, +1),
        U=(0, -1),
    )

    def print_map(only_visited=False):
        for x in range(w):
            for y in range(w):
                if only_visited:
                    if visited[x, y]:
                        print(".", end="")
                    else:
                        print("░", end="")
                else:
                    if [x, y] == head:
                        print("H", end="")
                    elif [x, y] == tail:
                        print("T", end="")
                    elif [x, y] == start:
                        print("s", end="")
                    elif visited[x, y]:
                        print(".", end="")
                    else:
                        print("░", end="")

            print()
        print()

    with open("input.txt") as f:
        for i, l in enumerate(f):
            print("\nMovement:", l, end="")
            v = int(l[2:-1])

            for j in range(v):
                ax, inc = dirs[l[0]]

                if head[ax ^ 1] == tail[ax ^ 1]:
                    if head[ax] == tail[ax] - inc:
                        tail[ax] = head[ax] + inc
                    else:
                        tail[ax] = head[ax]
                elif (head[ax] - tail[ax]) * inc > 0:
                    tail[ax] = head[ax]
                    tail[ax ^ 1] = head[ax ^ 1]

                head[ax] += inc

                visited[tail[0]][tail[1]] = True

        #print_map(True)
        print(np.count_nonzero(visited))


if __name__ == "__main__":
    main()
