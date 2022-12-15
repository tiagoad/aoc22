def main():
    total_strength = 0

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
                cycle += 1
                if inst == "addx":
                    x += v[0]

                if (cycle == 20) or (cycle % 40 == 20):
                    total_strength += cycle * x

            pipeline = []

    print(total_strength)


if __name__ == "__main__":
    main()
