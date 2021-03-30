from university_incomplete import count_countries, sort_by_chosen_score
import unittest


class TestCountCountries(unittest.TestCase):
    def test_count_countires(self):
        data = [{'country': 'US', 'foo': 42}, {'country': 'US', 'bar': 99}, {'country': 'Canada'}]
        expected = [('US', 2), ('Canada', 1)]

        result = count_countries(data)
        self.assertListEqual(expected, result)


class TestSortByChosenScore(unittest.TestCase):
    def test_sort_by_chosen_score(self):
        data = [{'foo': 42, 'bar': '99'},
                {'foo': 0, 'bar': '888'},
                {'foo': 0, 'bar': 0},
                {'foo': 0, 'bar': '-5'}]

        sorted_list = sort_by_chosen_score(data, 'bar')

        expected = [{'foo': 0, 'bar': '888'},
                    {'foo': 42, 'bar': '99'},
                    {'foo': 0, 'bar': 0},
                    {'foo': 0, 'bar': '-5'}]

        self.assertListEqual(sorted_list, expected)


if __name__ == "__main__":
    unittest.main()
