import pytest
from contextlib import nullcontext as no_raise_exception

class TestFloat:
    @pytest.mark.parametrize("x, y, res, expectation",
                             [(1.0, 2.0, 3.0, no_raise_exception()),
                              (2.0, 3, 5.0, no_raise_exception()),
                              (3.0, "4.0", TypeError, pytest.raises(TypeError))])
    def test_float_sum(self, x, y, res, expectation):
        with expectation:
            res = x+y
            assert isinstance(res, float)

    @pytest.mark.parametrize("x, y, res, expectation",
                             [(5.0, 2.5, 2.0, no_raise_exception()),
                              (6.0, 3, 2.0, no_raise_exception()),
                              (8.0, 2, 4.0, no_raise_exception()),
                              (3.0, 0, ZeroDivisionError, pytest.raises(ZeroDivisionError))])
    def test_float_div(self, x, y, res, expectation):
        with expectation:
            res = x/y
            assert isinstance(res, float)

class TestDict:
    def test_dict_key(self):
        players_contracts = {"Luka Doncic": "Dallas Mavericks",
                                  "Lebron James": "LA Lakers",
                                  "Joel Embid": "Phila 76"}
        assert players_contracts["Lebron James"] == "LA Lakers"

    @pytest.mark.parametrize("dict, value, key, expectation",
            [
                ({"Luka Doncic": "Dallas Mavericks", "Lebron James": "LA Lakers", "Joel Embid": "Phila 76"}, "Phila 76","Joel Embid", no_raise_exception()),
                ({"Luka Doncic": "Dallas Mavericks", "Lebron James": "LA Lakers", "Joel Embid": "Phila 76"}, "Atlanta Hawks", "Luka Doncic", pytest.raises(AssertionError))
            ])
    def test_dict_key_parametrized(self, dict, value, key, expectation):
        with expectation:
            assert dict[key] == value

class TestList:
    @pytest.mark.parametrize("x, expectation",
                             [(666, no_raise_exception()),
                              ("zxc", no_raise_exception()),
                              ([], no_raise_exception())])
    def test_list_append(self, x, expectation):
        with expectation:
            l = []
            l.append(x)
            expected = [x]
            assert l == expected

    @pytest.mark.parametrize("lst, index, expectation",
                             [([1, 2, 3], 1, no_raise_exception()),
                              ([1, 2, 3], 5, pytest.raises(IndexError))])
    def test_list_index_access(self, lst, index, expectation):
        with expectation:
            value = lst[index]
            assert isinstance(value, int)

