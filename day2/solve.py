#     r p s
#     X Y Z
# r A - W L
# p B L - W
# s C W L -

def p1(a, b):
    outcome = (b - a - 2) % 3  # L = 0, D = 1, W = 2
    outcome_score = outcome * 3
    shape_score = b
    return outcome_score + shape_score


def p2(a, outcome):
    outcome -= 1
    b = 1 + (a + outcome + 1) % 3
    outcome_score = outcome * 3
    shape_score = b
    return outcome_score + shape_score


def main():
    with open("input.txt") as f:
        p1total = 0
        p2total = 0

        while True:
            l = f.read(4)
            if l == "":
                break

            a = ord(l[0]) - 64  # 1|2|3
            b = ord(l[2]) - 87  # 1|2|3
            p1total += p1(a, b)
            p2total += p2(a, b)

        print("[P1] Total score:", p1total)
        print("[P2] Total score:", p2total)


if __name__ == "__main__":
    main()
