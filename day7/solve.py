import dataclasses
import typing


@dataclasses.dataclass
class File:
    size: int


@dataclasses.dataclass
class Dir:
    parent: typing.Union['Dir', None]
    children: typing.Dict[str, typing.Union['Dir', File]]


def build_tree(f):
    root = Dir(parent=None, children=dict())
    head = root

    f.__next__()
    for l in f:
        match l[0]:
            case "$" if l[2] == "c" and l[5] == ".":
                head = head.parent

            case "$" if l[2] == "c":
                if l[5:] not in head.children:
                    head.children[l[5:-1]] = Dir(parent=head, children={})
                head = head.children[l[5:-1]]

            case "$" if l[2] == "l":
                pass

            case "d":
                pass

            case _:
                size, fn = l[:-1].split(" ")
                head.children[fn] = File(size=int(size))

    return root


def solve_p1(root: Dir):
    acc = 0

    def find_dirs_p1(d: Dir):
        nonlocal acc

        size = 0
        for child in d.children.values():
            if hasattr(child, "size"):
                size += child.size
            else:
                size += find_dirs_p1(child)

        if size < 100000:
            acc += size

        return size

    find_dirs_p1(root)

    return acc


def main():
    with open('input.txt') as f:
        tree = build_tree(f)
        print(solve_p1(tree))


if __name__ == "__main__":
    main()
