import pytest

from table_data_operations import TableData


@pytest.fixture(scope='session', autouse=True)
def preparing_data_for_test():
    table_data_instance = TableData()
    return table_data_instance.load_table_data()
