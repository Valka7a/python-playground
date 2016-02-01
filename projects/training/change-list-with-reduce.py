words = ["apples", "bananas", "cantaloupes"]

def fix_list(list):
    return reduce(lambda all, list: all + list + ", ", list, '"') + '"'

print fix_list(words)
