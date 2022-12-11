ORD_A = ord('A')
ORD_a = ord('a')


def prio(n):
    on = ord(n)
    return (on - ORD_A + 26 if on < ORD_a else on - ORD_a) + 1


def p1(l):
    mid = len(l) // 2
    a, b = l[:mid], l[mid:]

    found = [False] * 53

    for it in a:
        ip = prio(it)
        found[ip] = True

    for it in b:
        ip = prio(it)
        if found[ip]:
            return ip

    return 0


def p2(ls):
    found = [0] * 53

    for li, l in enumerate(ls, 1):
        for it in l:
            ip = prio(it)
            if li == 1 or found[ip] == li:
                if li == 3:
                    return ip
                else:
                    found[ip] = li + 1

    return 0


def main():
    with open("input.txt") as f:
        p1total = 0
        p2total = 0

        ls = []
        for l in f:
            l = l[:-1]

            # part 1
            p1total += p1(l)

            # part 2
            ls.append(l)
            if len(ls) == 3:
                p2total += p2(ls)
                ls = []

        print("[P1] Total priorities:", p1total)
        print("[P2] Total priorities:", p2total)


if __name__ == "__main__":
    main()
