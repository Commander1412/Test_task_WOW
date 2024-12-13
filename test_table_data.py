import pytest

from table_data_operations import TableData


thresholds = [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9]


@pytest.mark.parametrize("threshold", thresholds)
def test_popularity_threshold(threshold, preparing_data_for_test):
    table_data = TableData()
    table_data.popularity_should_be_greater_than_threshold(threshold, preparing_data_for_test)
