from university_finished import count_countries, sort_by_chosen_score


def test_count_countires():
    data = [{'country': 'US', 'foo': 42}, {'country': 'US', 'bar': 99}, {'country': 'Canada'}]
    expected = [('US', 2), ('Canada', 1)]

    result = count_countries(data)
    assert expected == result


def test_sort_by_chosen_score():
    data = [{'foo': 42, 'bar': '99'},
            {'foo': 0, 'bar': '888'},
            {'foo': 0, 'bar': 0},
            {'foo': 0, 'bar': '-5'}]

    sorted_list = sort_by_chosen_score(data, 'bar')

    expected = [{'foo': 0, 'bar': '888'},
                {'foo': 42, 'bar': '99'},
                {'foo': 0, 'bar': 0},
                {'foo': 0, 'bar': '-5'}]

    for i, kv in enumerate(sorted_list):
        expected_kv = expected[i]
        if kv != expected_kv:
            print('Error - Items are not equal')
            print(kv, expected_kv)
            assert kv == expected_kv


if __name__ == "__main__":
    # run in python to avoid pytest dependency
    test_count_countires()
    test_sort_by_chosen_score()
    print('Tests pass')
