from my_stats import my_median

def test_my_median():
    data = [1, 2, 3, 4, 5]
    assert my_median(data) == 3

    data = [1, 2, 3, 4, 5, 6]
    assert my_median(data) == 3.5

    data = [1, 6, 17]
    assert my_median(data) == 6

def main():
    test_my_median()

if __name__ == '__main__':
    main()