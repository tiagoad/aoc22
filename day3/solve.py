ORD_A = ord('A')
ORD_a = ord('a')
FOUND_ARR = [False] * 53


def prio(n):
    on = ord(n)
    return (on - ORD_A + 26 if on < ORD_a else on - ORD_a) + 1


def main():
    with open("input.txt") as f:
        total = 0

        for l in f:
            l = l[:-1]
            mid = len(l) // 2
            a, b = l[:mid], l[mid:]

            found = [*FOUND_ARR]

            for it in a:
                ip = prio(it)
                found[ip] = True

            for it in b:
                ip = prio(it)
                if found[ip]:
                    total += ip
                    break

        print("Total priorities:", total)


if __name__ == "__main__":
    main()
