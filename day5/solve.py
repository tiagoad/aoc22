import copy


def main():
    with open('input.txt') as f:
        stacks = []

        for l in f:
            l = l[:-1]
            ll = len(l)
            if ll == 0:
                break

            for i, ci in enumerate(range(1, ll, 4)):
                if l[ci] != " " and ord(l[ci]) >= 65:
                    for si in range(len(stacks), i + 1):
                        stacks.append([])

                    stacks[i].append(l[ci])

        p1stacks = copy.deepcopy(stacks)
        p2stacks = copy.deepcopy(stacks)

        for l in f:
            spl = l.split(" ")
            it = int(spl[1])
            a = int(spl[3]) - 1
            b = int(spl[5]) - 1

            # part 1
            p1stacks[b] = list(reversed(p1stacks[a][:it])) + p1stacks[b]
            p1stacks[a] = p1stacks[a][it:]

            # part 2
            p2stacks[b] = list(p2stacks[a][:it]) + p2stacks[b]
            p2stacks[a] = p2stacks[a][it:]

        p1output = ""
        for s in p1stacks:
            if len(s) > 0:
                p1output += s[0]

        p2output = ""
        for s in p2stacks:
            if len(s) > 0:
                p2output += s[0]

        print("[P1]", p1output)
        print("[P2]", p2output)


if __name__ == "__main__":
    main()
