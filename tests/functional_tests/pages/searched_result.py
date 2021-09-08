from tests.functional_tests.pages.base_class import base_class
import re


class Result_Page(base_class):

    def __init__(self, driver):
        self.driver = driver
        self.common_config = self.get_config('common')
        self.config_result = self.get_config('seach_result')
        print("==")

    def validate_search_result_header(self):
        # Make use of reg ex in python to mock below string
        # 1-12 of 505 results for "samsung mobiles"
        try:
            # pattern = r"^1.[0-9]+\s.+[0-9]+\s.+[A-Z].*"
            pattern = r"^1.[0-9]+\s.+[0-9]+\s.+[a-z].*"
            element1 = self.driver.find_element_by_xpath(self.config_result['search_result_header_xpath_1'])
            element2 = self.driver.find_element_by_xpath(self.config_result['search_result_header_xpath_2'])
            headerTxt = element1.text + element2.text
            result = re.match(pattern, headerTxt)
            print(result)
            print(headerTxt + pattern)
            if result:
                print("Matched")
            else:
                print("Not Matched")
            return result
        except Exception as e:
            print(str(e))
            return False

    def validate_search_result_body(self):
        searched_items = self.driver.find_elements_by_xpath(self.config_result['searched_items_xpath'])
        return len(searched_items) > 1
        pass

    def open_an_item(self, item_name=None, which_item=1):
        searched_items = self.driver.find_elements_by_xpath(self.config_result['searched_items_xpath'])
        item = searched_items.__getitem__(which_item)
        item.click()
        return True
