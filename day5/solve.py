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

        for l in f:
            spl = l.split(" ")
            it = int(spl[1])
            a = int(spl[3]) - 1
            b = int(spl[5]) - 1

            stacks[b] = list(reversed(stacks[a][:it])) + stacks[b]
            stacks[a] = stacks[a][it:]

        output = ""
        for s in stacks:
            if len(s) > 0:
                output += s[0]

        print(output)



if __name__ == "__main__":
    main()
