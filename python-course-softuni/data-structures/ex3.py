# User input
name = input('Enter your name: ')

# Check if empty
if name == '':
    print("Invalid input.")
    exit()

# Get only uppercase
capitals = filter(lambda x: x.isupper(), name)

# Make capitals a list
capitals = list(capitals)

if len(capitals) > 0:
    print('.'.join(capitals) + '.')
else:
    print("Invalid input.")
