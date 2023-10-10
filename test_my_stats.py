import pytest
from my_stats import my_median

def test_my_median():
    data = [1, 2, 3, 4, 5]
    assert my_median(data) == 3

    data = [1, 2, 3, 4, 5, 6]
    assert my_median(data) == 3.5

    data = [1, 6, 17]
    assert my_median(data) == 6


def test_my_median_empty():
    data = []
    with pytest.raises(ValueError, match=r".*empty.*"):
        my_median(data)

@pytest.mark.parametrize("my_list, expected", [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5, 6], 3.5),
    ([1, 6, 17], 6),
    ([1, 6, 17, 2, 3], 3)
])
def test_my_median_par(my_list, expected):
    assert my_median(my_list) == expected


def main():
    test_my_median()

if __name__ == '__main__':
    main()