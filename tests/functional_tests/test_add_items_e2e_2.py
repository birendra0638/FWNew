import math
import os
import time

import pandas as pd
from tests.functional_tests.pages.home_page import Home_Page
from tests.functional_tests.pages.searched_result import Result_Page
from selenium import webdriver
import pytest

#

test_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', "./fixtures/testdata/ecom_data.xls"))
dataframe = pd.read_excel(test_data_path, sheet_name="Test_AddItems_ToCart_E2E", header=0, index_col=None)
dataframe = dataframe.fillna('')
# wb_obj = openpyxl.load_workbook(test_data_path)
# sheet = wb_obj.get_sheet_by_name("Test_Search_Results", header = 0, index_col=None)
# dataframe = pd.DataFrame(sheet.values)

dataframe = dataframe[dataframe["Execute"] == "YES"]
testParams = []
testId = []

for i, row in dataframe.iterrows():
    testParams.append((row['Product'], row['AddToCart'], row['SearchFilter'], row['Qty'], row['DeleteFromCart'])),
    testId.append(row['ID'])


class Test_AddItems_ToCart_E2E(object):

    def setup_class(self):
        self.home_page = Home_Page(self.browser, self.xlsx_utility, self.xls_utility)
        self.result_page = Result_Page(self.driver)

    @pytest.fixture
    def clean_up(self):
        print("@@@inside fixture")

    #############################################################################
    # Test case name: Validate guest user
    # Test case id: E2E_01_Prerequisite
    # Test case description: Check that user is logged-in as guest or not
    # Author: Birendra
    # Date: 06-Aug-21
    #############################################################################
    @pytest.mark.dependency()
    def test_guest_user(self):
        # To validate surfing as a guest or not
        user = self.home_page.get_user()
        assert user == "Hello, Sign in"

    #############################################################################
    # E2E Test case name: Add items as a guest to cart
    # Test case id: E2E_01
    # Test case description: Search items as guest, search using filter options,
    #                        pick items based on filers, change the quantity and
    #                        add items to cart
    # Author: Birendra
    # Date: 06-Aug-21
    #############################################################################
    @pytest.mark.parametrize("Product,AddToCart,SearchFilter,Qty,DeleteFromCart", testParams, ids=testId)
    @pytest.mark.usefixtures('clean_up')
    def test_add_item_to_cart_e2e(self, Product, AddToCart, SearchFilter, Qty, DeleteFromCart):
        print("inside test_add_item_to_cart_e2e")
        if SearchFilter != '':
            assert self.home_page.select_a_filter(SearchFilter)

        assert self.home_page.search_product(Product)
        assert self.home_page.pick_an_item()
        # assert self.home_page.pick_an_item(item_index=5)
        # assert self.home_page.pick_an_item(item_name=Product+" f22")
        # self.result_page.validate_result()

        # ASSIGNMENT FOR YOU TO DEVELOP
        assert self.result_page.validate_search_result_header()
        assert self.result_page.validate_search_result_body()
        assert self.result_page.open_an_item()

        #     print("--")
        #     pass
        #
        #
        # for i, row in self.data_frame.iterrows():
        #     # if not math.isnan(float(row['SearchFilter'])):
        #     #     pass
        #     if row['SearchFilter'] != '':
        #         print("--")
        #         pass
        #     assert self.home_page.search_product(str(row['Product']))  # self.data_frame.columns[i]
        #     self.home_page.pick_an_item()
        #     # self.result_page.validate_result()
        #     if row['AddToCart'] == 'YES':
        #         print("###")
