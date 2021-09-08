import os
import time
from tests.functional_tests.pages.home_page import Home_Page
from selenium import webdriver
import pytest
# testData = os.path.abspath('')
# df = pandas.read_excel()


class Test_Search_Products(object):

    def setup_class(self):
        self.home_page = Home_Page(self.browser, self.xlsx_utility, self.xls_utility)
        self.data_frame1 = self.home_page.xls_utility.read_file(sheet_name=os.environ.get('PYTEST_CURRENT_TEST').split('::')[1])
        # print(self.xls_utility.read_df)
        self.data_frame2 = self.home_page.xlsx_utility.read_specific_data(2,1,3,6, sheet_name=os.environ.get('PYTEST_CURRENT_TEST').split('::')[1])
        self.specific_cell = self.home_page.xlsx_utility.read_single_cell(2, 3, 'Test_Search_Products')
        print(self.URL)
        print(self.env)

    # Decorators
    @pytest.fixture
    # @pytest.fixture(scope='class', autouse=True)
    # @pytest.yield_fixture(scope='function')
    def clean_up(self):
        print("@@@inside fixture")

    @pytest.mark.usefixtures('clean_up') # 1st way of calling fixture
    def test_search_product(self):
        print("inside test_product")
        assert self.home_page.check_banner()
        product_series = self.data_frame1['Product']
        for i, row in self.data_frame.iterrows():
            assert self.home_page.search_product(str(row['Product']))#self.data_frame.columns[i]

    def test_search_product_with_filter(self, clean_up):
        print("inside test_product_with_filter")
        self.data_frame = self.data_frame1[self.data_frame1['Filter'].notna()]
        for i, row in self.data_frame.iterrows():
            assert self.home_page.select_filter()
            assert self.home_page.search_product(str(row['Product']))

    def test_select_product_and_validate_search_result(self):
        print("inside test_select_product_and_validate_search_result")
        #implement this test

    @pytest.fixture(scope='class', autouse=True)
    def class_settings(self):
        print("@@@inside class fixture")
        #login


    # def teardown_class(self):
    #     print("Tear down")