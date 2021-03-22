"""
A finished and working version of the program
"""


from csv import DictReader
from collections import Counter


def read_university():
    """
    Read the university file
    :return: generator to university records (dicts)
    """

    filename = "university_data.csv"

    # TODO: remove duplicates, keep the first

    for row in DictReader(open(filename, 'r')):
        name = row['university_name']

        if row['country'] == 'United States of America':
            row['country'] = 'US'

        yield row


def count_countries(data):
    """
    Count countries. E.g.
    [{country: 'US}, {country: 'US}, {country: 'Canada'} ->
    [('US', 2), ('Canada', 1)]
    :param data: iterable of university records
    :return: list of (country, number) tuples where number
        is the number of records in data having that country
        in the 'country' key
        sorted by number, largest first
    """
    # TODO: finish
    return []


def print_university(rank, university):
    """
    Print out a university record in a nice readable format
    :param rank: Rank, a number
    :param university: university record
    :return: None
    """

    message = "{rank} {univ}, {country}: teaching: {teach}, international: " \
              "{intern}, research: {res} Fem./Male: {mf}"

    rank = str(rank).zfill(2)

    print(message.format(univ=university['university_name'],
                         teach=university['teaching_score'],
                         intern=university['international_score'],
                         res=university['research_score'],
                         mf=university['female_male_ratio'],
                         country=university['country'],
                         rank=rank))


def prompt_for_preferred_country(country_count_items):
    """
    Prompt for choice of country, return the country name chosen
    :param country_count_items: list of country count items
        output of count_countries
    :return: country name
    """
    # Choose the country you prefer
    message = "Choose a country: "

    for index, item in enumerate(country_count_items):
        country, count = item
        message += "\n %s, %s, (N_universities=%s)" % (index, country, count)

    message += '\n'

    # prompt for the index of the preferred country
    index = int(input(message))

    country = country_count_items[index][0]
    num_univ = country_count_items[index][1]

    print('Country = %s, N_Universities: %s' % (country, num_univ))

    return country


def more_males(female_male_ratio_string):
    """
    Take a female_to_male_ratio string and return
    True if there are more males. Return False otherwise.
    E.g. '50:49:01' -> False, '49:50:01' -> True
    Return True if the string is empty or otherwise unparsable

    The strings look like
    :param female_male_ratio_string:
    :return:
    """
    res = female_male_ratio_string.split(':')

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


def filter_based_on_gender_stats(universities):
    """
    Filter the list of university records depending on
        the gender statistics
    :param universities: list of university records
    :return: filtered list
    """
    message = "Prefer: More males [0], More females [1] or Don't Care [2]\n"
    index = int(input(message))

    # default if do not care
    univ = [u for u in universities]

    if index == 0:
        # for more males choice
        univ = [u for u in universities if more_males(u['female_male_ratio'])]

    if index == 1:
        # for more females choice
        univ = [u for u in universities if not more_males(u['female_male_ratio'])]

    return univ


def prompt_for_chosen_score():
    """
    Prompt for the type of score (teaching, international, research)
        that the universities should be ranked
    :return: the chosen score name
    """

    choices = ['teaching_score', 'international_score', 'research_score']
    lookup = {i: c for i, c in enumerate(choices)}

    message = 'rank by: '
    for items in lookup.items():
        message += "%s [%s], " % (items[1], items[0])

    message += '\n'

    index = int(input(message))

    return lookup[index]


def sort_by_chosen_score(univ, chosen_score):
    """
    Sort the universities by the chosen score, highest first
    :param univ: list of university records
    :param chosen_score: the chosen score to rank by
    :return: sorted list
    """
    # TODO: finish
    return []


def main():
    """
    Run the main program
    :return:
    """
    data = list(read_university())

    # Get country count stats
    country_count_items = count_countries(data)

    # prompt for chosen country
    country = prompt_for_preferred_country(country_count_items)

    # filter for the Universities being in the preferred country
    universities = [i for i in data if i['country'] == country]

    # Chose whether you prefer more males or females or do not care
    univ = filter_based_on_gender_stats(universities)

    # Choose how to rank them. Prompt for choice between
    # teaching, international or research
    chosen_score = prompt_for_chosen_score()
    univ_sorted = sort_by_chosen_score(univ, chosen_score)

    # Print them out, filtered and ranked in this way

    print('\nTop Universities\n-------------------')

    for rank, u in enumerate(univ_sorted):
        print_university(rank + 1, u)


if __name__ == "__main__":
    main()
