import itertools
import json


def compare(a, b):
    if type(a) == int and type(b) == int:
        if a == b:
            return None
        else:
            return a < b

    elif type(a) == int:
        a = [a]

    elif type(b) == int:
        b = [b]

    for a2, b2 in zip(a, b):
        r = compare(a2, b2)
        if r is not None:
            return r

    if len(a) > len(b):
        return False

    elif len(a) < len(b):
        return True

    else:
        return None


def main():
    right_pairs = []

    with open("input.txt") as f:
        for i in itertools.count(start=1):
            a = f.readline()[:-1]
            b = f.readline()[:-1]
            f.readline()
            if a == "":
                break

            if compare(json.loads(a), json.loads(b)):
                right_pairs.append(i)

    print("[P1]", sum(right_pairs))


if __name__ == "__main__":
    main()
