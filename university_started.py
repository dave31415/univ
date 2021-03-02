# A started code file with some pieces to be added
# candidate starts with this and can see a running example of the other


def run():
    # get the data as a list of dictionaries
    data = None

    items = count_countries(data)

    message = "Choose a country: "

    for index, item in enumerate(items):
        country, count = item
        message += "\n %s, %s, (N_universities=%s)" % (index, country, count)

    message += '\n'

    index = int(input(message))
    country = items[index][0]
    num_univ = items[index][1]

    print('Country = %s, N_Universities: %s' % (country, num_univ))

    universities_in_country = [i for i in data if i['country'] == country]

    message = "Prefer: More males [0], More females [1] or Don't Care [2]\n"
    index = int(input(message))

    # if Don't care
    univ = universities_in_country

    if index == 0:
        univ = [u for u in universities_in_country if more_males(u['female_male_ratio'])]

    if index == 1:
        univ = [u for u in universities_in_country if not more_males(u['female_male_ratio'])]

    choices = ['teaching_score', 'international_score', 'research_score']
    lookup = {i: c for i, c in enumerate(choices)}

    message = 'rank by: '
    for items in lookup.items():
        message += "%s [%s], " % (items[1], items[0])

    message += '\n'

    index = int(input(message))

    # FINISH


if __name__ == "__main__":
    run()
