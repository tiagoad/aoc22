import functools


def solve(buff_size=4):
    with open('input.txt') as f:
        for l in f:
            buff = [None] * buff_size
            when = None

            for i, chr in enumerate(l):
                if chr == "\n":
                    break

                buff[i%buff_size] = chr
                if i < buff_size-1:
                    continue

                try:
                    sorted(buff, key=functools.cmp_to_key(lambda a, b: ord(b) - ord(a) if a != b else None))
                except TypeError:
                    pass
                else:
                    when = i+1
                    break

            return when


def main():
    print("[P1]", solve(4))
    print("[P1]", solve(14))


if __name__ == "__main__":
    main()
