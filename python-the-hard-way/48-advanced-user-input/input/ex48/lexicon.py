directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'in']
nouns = ['door', 'bear', 'princess', 'cabinet']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def scan(words):

	word = words.split()
	sentence = []

	for i in word:
		if i in directions:
			sentence.append(('direction', i))

		elif i in verbs:
			sentence.append(('verb', i))

		elif i in stops:
			sentence.append(('stop', i))

		elif i in nouns:
			sentence.append(('noun', i))

		elif i.isdigit():
			sentence.append(('number', convert_number(i)))

		else:
			sentence.append(('error', i))

	return sentence

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
