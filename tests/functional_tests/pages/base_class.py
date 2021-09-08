import json
import os


class base_class(object):

    def __init__(self):
        pass

    def get_config(self, page):
        filepath = os.path.abspath(os.path.dirname(__file__))
        element_file = os.path.join(str(filepath), 'elements.json')
        with open(str(element_file)) as json_data_file:
            data_file = json.load(json_data_file)
        return data_file[page]


    def search_product(self, product_keyword):
        print("search_product")
        self.driver.find_element_by_id(self.common_config['search_text_box_id']).clear()
        self.driver.find_element_by_id(self.common_config['search_text_box_id']).send_keys(product_keyword)
        return True
        #write your code for waiting until the picklist appears

    def select_filter(self):
        print("Inside select_filter")
        return True
        #write your code for selecting filter

