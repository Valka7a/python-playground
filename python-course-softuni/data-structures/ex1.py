# User input
sentence = input('Write sentence: ')

# Cun text to 10th elements and ellipsis to the end
if len(sentence) > 10:
    sentence = sentence[:10] + '...'

print(sentence)
