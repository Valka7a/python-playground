people = [
    {
        'name': "Мария",
        'interests': ['пътуване', 'танци', 'плуване', 'кино'],
        'gender': "female",
    },
    {
        'name': "Диана",
        'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
        'gender': "female",
    },
    {
        'name': "Дарина",
        'interests': ['танци', 'покер', 'история', 'софтуер'],
        'gender': "female",
    },
    {
        'name': "Лилия",
        'interests': ['покер', 'автомобили', 'танци', 'кино'],
        'gender': "female",
    },
    {
        'name': "Галя",
        'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
        'gender': "female",
    },
    {
        'name': "Валерия",
        'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
        'gender': "female",
    },
    {
        'name': "Ина",
        'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
        'gender': "female",
    },
    {
        'name': "Кирил",
        'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
        'gender': "male",
    },
    {
        'name': "Георги",
        'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
        'gender': "male",
    },
    {
        'name': "Андрей",
        'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
        'gender': "male",
    },
    {
        'name': "Емил",
        'interests': ['летене', 'баскетбол', 'софтуер', 'наука'],
        'gender': "male",
    },
    {
        'name': "Димитър",
        'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
        'gender': "male",
    },
    {
        'name': "Петър",
        'interests': ['пътуване', 'покер', 'баскетбол', 'лов със соколи'],
        'gender': "male",
    },
    {
        'name': "Калоян",
        'interests': ['история', 'покер', 'пътуване', 'автомобили'],
        'gender': "male",
    },
]

# Filter the males and females from people list
men = list(filter(lambda person: person['gender'] == 'male', people))
women = list(filter(lambda person: person['gender'] == 'female', people))

for male in men:
    for female in women:
        men_interests = set(male['interests'])
        women_interests = set(female['interests'])

        intersection = men_interests.intersection(women_interests)

        if intersection:
            print("{} и {} - интереси: {}".format(
                male['name'],
                female['name'],
                ', '.join(intersection)
            ))
