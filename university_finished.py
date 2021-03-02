from csv import DictReader
from collections import Counter


def read_university():
    filename = "/Users/david/university_data.csv"
    return DictReader(open(filename, 'r'))


def count_countries(data):
    count = Counter()
    for row in data:
        count[row['country']] += 1

    items = sorted(count.most_common(), key=lambda x: -x[1])

    return items


def more_males(female_male_ratio):
    res = female_male_ratio.split(':')
    if len(res) >= 2:
        male = res[0]
        female = res[1]
    else:
        return True
    try:
        if int(male) > int(female):
            return True
        else:
            return False
    except ValueError:
        print('error converting ratio: ', female_male_ratio)
        return True


def run():
    data = list(read_university())

    message = "Choose a country: "

    items = count_countries(data)

    for index, item in enumerate(items):
        country, count = item
        message += "\n %s, %s, (N_universities=%s)" % (index, country, count)

    message += '\n'

    index = int(input(message))
    country = items[index][0]
    num_univ = items[index][1]

    print('Country = %s, N_Universities: %s' % (country, num_univ))

    universities = [i for i in data if i['country'] == country]

    message = "Prefer: More males [0], More females [1] or Don't Care [2]\n"
    index = int(input(message))

    univ = universities

    if index == 0:
        univ = [u for u in universities if more_males(u['female_male_ratio'])]

    if index == 1:
        univ = [u for u in universities if not more_males(u['female_male_ratio'])]

    choices = ['teaching_score', 'international_score', 'research_score']
    lookup = {i: c for i, c in enumerate(choices)}

    message = 'rank by: '
    for items in lookup.items():
        message += "%s [%s], " % (items[1], items[0])

    message += '\n'

    index = int(input(message))

    val = lookup[index]
    univ_sorted = sorted(univ, key=lambda x: -float(x[val]))

    for u in univ_sorted:
        print(u)


if __name__ == "__main__":
    run()
