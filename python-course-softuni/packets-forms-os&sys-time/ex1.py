import sys

def find_file(dir, filename):


if len(sys.argv) < 3:
    print("Please provide at least 3 parameters")
else:
    find_file(dir=sys.argv[1], filename=sys.argv[2])

print(sys.argv)