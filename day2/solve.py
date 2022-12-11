#     r p s
#     X Y Z
# r A - W L
# p B L - W
# s C W L -

def p1(a, b):
    outcome = (b - a - 2) % 3
    outcome_score = outcome * 3
    shape_score = b
    return outcome_score + shape_score


def main():
    with open("input.txt") as f:
        p1total = 0

        while True:
            l = f.read(4)
            if l == "":
                break

            a = ord(l[0]) - 64  # 1|2|3
            b = ord(l[2]) - 87  # 1|2|3
            p1total += p1(a, b)

        print("Total score:", p1total)


if __name__ == "__main__":
    main()
