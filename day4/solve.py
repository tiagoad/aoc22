def main():
    with open('input.txt') as f:
        overlap_total = 0
        overlap_partial = 0

        for l in f:
            l = l[:-1]

            a, b = l.split(",")
            a1, a2 = map(int, a.split("-"))
            b1, b2 = map(int, b.split("-"))

            if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
                overlap_total += 1

            if (b2 >= a1 >= b1) or (a2 >= b1 >= a1):
                overlap_partial += 1

        print("[P1] Total overlaps:", overlap_total)
        print("[P2] Partial overlaps:", overlap_partial)


if __name__ == "__main__":
    main()
