import numpy as np


def main():
    w = 40
    h = 6
    crt = np.zeros((h, w), dtype=bool)
    total_strength = 0

    def print_crt():
        out = ""
        for l in crt:
            for px in l:
                out += "#" if px else " "
            out += "\n"
        return out

    with open("input.txt") as f:
        x = 1
        cycle = 1
        pipeline = []

        for l in f:
            match l[0:4]:
                case "addx":
                    pipeline += [["noop"], ["addx", int(l[5:-1])]]

                case "noop":
                    pipeline += [["noop"]]

            for [inst, *v] in pipeline:
                crt_x = (cycle - 1) % w
                crt_y = (cycle - 1) // w

                if abs(x - crt_x) <= 1:
                    crt[crt_y][crt_x] = True

                cycle += 1
                if inst == "addx":
                    x += v[0]

                if (cycle == 20) or (cycle % 40 == 20):
                    total_strength += cycle * x

            pipeline = []

    print("[P1]", total_strength)
    print("[P2]\n" + print_crt())


if __name__ == "__main__":
    main()
