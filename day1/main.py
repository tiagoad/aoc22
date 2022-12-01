with open("input.txt") as f:
    data = f.read()

groups = data.strip().split("\n\n")
summed = map(lambda e: sum(map(int, e.split("\n"))), groups)
ranked = sorted(summed, reverse=True)

print("Top 1:", ranked[0])
print("Top 3:", sum(ranked[0:3]))