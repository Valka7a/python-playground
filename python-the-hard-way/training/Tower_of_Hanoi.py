#disks = int(raw_input())
#source = range(1, disks + 1)
"""
def tower_of_hanoi(disks, source, helper = [], target = []):
    if disks > 0:
        tower_of_hanoi(disks - 1, source, target, helper)
        if source:
            target.append(source.pop())
        tower_of_hanoi(disks - 1, helper, source, target)

    return target
disks = int(raw_input())
source = range(disks, 0, - 1)
print tower_of_hanoi(disks, source)

"""
def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)

x = input()
source = range(x, 0, -1)
target = []
helper = []
hanoi(len(source),source,helper,target)

print source, helper, target
