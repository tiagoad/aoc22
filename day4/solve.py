def main():
    with open('input.txt') as f:
        overlap_total = 0

        for l in f:
            l = l[:-1]

            a, b = l.split(",")
            a1, a2 = map(int, a.split("-"))
            b1, b2 = map(int, b.split("-"))

            if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
                overlap_total += 1

        print("Total overlaps:", overlap_total)


if __name__ == "__main__":
    main()
