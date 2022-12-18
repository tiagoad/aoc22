import functools
import itertools
import json


def compare(a, b):
    if type(a) == int and type(b) == int:
        if a == b:
            return 0
        else:
            return -1 if a < b else 1

    elif type(a) == int:
        a = [a]

    elif type(b) == int:
        b = [b]

    for a2, b2 in zip(a, b):
        r = compare(a2, b2)
        if r != 0:
            return r

    if len(a) > len(b):
        return 1

    elif len(a) < len(b):
        return -1

    else:
        return 0


def main():
    right_pairs = []
    dividers = [[[2]], [[6]]]
    pairs = dividers.copy()

    with open("input.txt") as f:
        for i in itertools.count(start=1):
            a = f.readline()[:-1]
            b = f.readline()[:-1]
            f.readline()
            if a == "":
                break

            a = json.loads(a)
            b = json.loads(b)

            if compare(a, b) == -1:
                right_pairs.append(i)

            pairs += [a, b]

    pairs.sort(key=functools.cmp_to_key(compare))
    s = 1
    for i, l in enumerate(pairs, start=1):
        if l in dividers:
            s *= i

    print("[P1]", sum(right_pairs))
    print("[P2]", s)


if __name__ == "__main__":
    main()
