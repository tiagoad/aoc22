def main():
    top_3 = get_top(3)
    print("Top 1:", top_3[0])
    print("Top 3:", sum(top_3))

def get_top(top_n):
    buff = [None] * top_n
    acc = 0

    def feed(l):
        nonlocal buff, acc

        try:
            # it's a number, add to the tally and carry on.
            acc += int(l)
        except:
            # it's not a number...
            for i, v in enumerate(buff):
                if (v is None) or (acc > v):
                    # ... and it's larger than the i'th item in the buffer.

                    # shift all this element to the right
                    for j in range(top_n-1, i, -1):
                        buff[j] = buff[j-1]

                    # and set it to the new value
                    buff[i] = acc

                    # break out of the loop
                    break
            
            acc = 0

    with open("input.txt") as f:
        for l in f:
            # process this line
            feed(l)

        # add a final newline so we don't skip the last group
        feed('\n')

    return buff

if __name__ == '__main__':
    main()