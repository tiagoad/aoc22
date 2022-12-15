import re


def main():
    with open("input.txt") as f:
        data = f.read()

    mit = re.finditer(
        r"""Monkey (?P<id>[0-9]+):
  Starting items: (?P<starting_items>(?:[0-9]+(?:, )?)+)
  Operation: new = (?P<op_a>\w+) (?P<op_sym>[*+]) (?P<op_b>\w+)
  Test: divisible by (?P<test>[0-9]+)
    If true: throw to monkey (?P<true_mnk>[0-9]+)
    If false: throw to monkey (?P<false_mnk>[0-9]+)""",
        data,
    )

    monkeys = []
    for m in mit:
        g = m.groupdict()
        g["items"] = list(map(int, g["starting_items"].split(", ")))
        g["op_a"] = None if g["op_a"] == "old" else int(g["op_a"])
        g["op_b"] = None if g["op_b"] == "old" else int(g["op_b"])
        g["true_mnk"] = int(g["true_mnk"])
        g["false_mnk"] = int(g["false_mnk"])
        g["test"] = int(g["test"])
        g["inspect_count"] = 0

        monkeys.append(g)

    for i in range(20):
        for m in monkeys:
            print(f"Monkey {m['id']}:")
            if len(m["items"]) == 0:
                print("  does nothing")
            while len(m["items"]) > 0:
                it = m["items"].pop(0)
                print(f"  inspects {it}")
                m["inspect_count"] += 1

                a = m["op_a"] if m["op_a"] else it
                b = m["op_b"] if m["op_b"] else it

                it = a + b if m["op_sym"] == "+" else a * b
                print(f"    {a} {m['op_sym']} {b} = {it}")

                it = it // 3
                print(f"    worry / 3 = {it}")

                if it % m["test"] == 0:
                    print(f"    divisible by {m['test']}")

                    monkeys[m["true_mnk"]]["items"].append(it)
                    print(f"    item {it} -> monkey {m['true_mnk']}")
                else:
                    print(f"    not divisible by {m['test']}")

                    monkeys[m["false_mnk"]]["items"].append(it)
                    print(f"    item {it} -> monkey {m['false_mnk']}")

    by_inspect_count = sorted(monkeys, key=lambda m: m["inspect_count"], reverse=True)

    monkey_business = 1
    for m in by_inspect_count[:2]:
        monkey_business *= m["inspect_count"]

    print("[P1]", monkey_business)


if __name__ == "__main__":
    main()
