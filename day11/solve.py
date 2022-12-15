import re
from functools import reduce


def parse_monkeys():
    with open("input.txt") as f:
        data = f.read()

    mit = re.finditer(
        r"""Monkey (?P<id>[0-9]+):
  Starting items: (?P<starting_items>(?:[0-9]+(?:, )?)+)
  Operation: new = old (?P<op_sym>[*+]) (?P<op_v>\w+)
  Test: divisible by (?P<test>[0-9]+)
    If true: throw to monkey (?P<true_mnk>[0-9]+)
    If false: throw to monkey (?P<false_mnk>[0-9]+)""",
        data,
    )

    monkeys = []
    for m in mit:
        g = m.groupdict()
        g["items"] = list(map(int, g["starting_items"].split(", ")))
        g["op_v"] = None if g["op_v"] == "old" else int(g["op_v"])
        g["true_mnk"] = int(g["true_mnk"])
        g["false_mnk"] = int(g["false_mnk"])
        g["test"] = int(g["test"])
        g["inspect_count"] = 0

        monkeys.append(g)

    return monkeys


def get_monkey_business(monkeys, part):
    divisor_product = reduce(lambda x, y: x*y, map(lambda m: m["test"], monkeys))

    for i in range(20 if part == 1 else 10000):
        for m in monkeys:
            while len(m["items"]) > 0:
                it = m["items"].pop(0)

                m["inspect_count"] += 1

                a = it
                b = m["op_v"]
                if b is not None:
                    if m["op_sym"] == "*":
                        it = a * b
                    else:
                        it = a + b
                else:
                    it = it * it

                if part == 1:
                    it = it // 3
                else:
                    it = divisor_product + it % divisor_product

                if it % m["test"] == 0:
                    next_m = monkeys[m["true_mnk"]]
                else:
                    next_m = monkeys[m["false_mnk"]]

                next_m["items"].append(it)

    by_inspect_count = sorted(monkeys, key=lambda m: m["inspect_count"], reverse=True)

    monkey_business = 1
    for m in by_inspect_count[:2]:
        monkey_business *= m["inspect_count"]

    return monkey_business


def main():
    print("[P1]", get_monkey_business(parse_monkeys(), part=1))
    print("[P2]", get_monkey_business(parse_monkeys(), part=2))


if __name__ == "__main__":
    main()
