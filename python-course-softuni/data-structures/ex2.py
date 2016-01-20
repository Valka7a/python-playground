# User input
text = input('Write some text: ')
delimiter = input('Write delimiter: ')

# If delimiter is empty just print text
if not delimiter:
    print(text)
    exit()

index = text.find(delimiter)

# Print message or print text after delimiter
if index == -1:
    print('Delimiter not found here.')
else:
    index += len(delimiter)
    print(text[index:])
