# Tower of Hanoi problem: Moving n disks from A to C (through B)
# Please print the specific steps


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)  # moving the top n-1 disks from a to b
        print("Moving the disk from %s to %s" % (a, c))  # moving the one left from a to c
        hanoi(n-1, b, a, c)  # moving all the n-1 disks from b to c


# test:
hanoi(5, "A", "B", "C")
# time complexity: O(2**n)
