# Interests
ivan = ['пушене', 'пиене', 'тия три неща', 'коли', 'facebook', 'разходки по плажа', 'скандинавска поезия', 'игри']
maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино']

# Collect common interests
common_interests = list(filter(lambda item: item in ivan, maria))

# Print common interests
print(common_interests)
