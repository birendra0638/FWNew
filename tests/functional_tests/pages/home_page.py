from tests.functional_tests.pages.base_class import base_class


class Home_Page(base_class):

    def __init__(self, driver, xlsx_utility, xls_utility=None):
        self.xlsx_utility = xlsx_utility
        self.xls_utility = xls_utility
        self.driver = driver
        self.common_config = self.get_config('common')
        self.home_config = self.get_config('home')
        print("==")

    #######################################################
    # Funtion name: check_banner
    # Objective: it will check the banner on the home page
    # Author: Birendra
    # Date: 7-AUG-2021
    ######################################################
    def check_banner(self):
        print("inside check_banner")
        return True

    #######################################################
    # Funtion name: check_banner
    # Objective: it will check the banner on the home page
    # Author: Birendra
    # Date: 7-AUG-2021
    ######################################################
    def get_user(self):
        print("inside get_user")
        return "Hello, Sign in"

    #######################################################
    # Funtion name: select_a_filter
    # Objective: it will select a filter for search
    # Author: Birendra
    # Date: 7-AUG-2021
    ######################################################
    def select_a_filter(self, filter):
        try:
            elem = self.driver.find_element_by_xpath(self.home_config['filter_dropdown_xpath'])
            elem.click()
            elem.find_element_by_xpath("./option[text()='" + filter + "']").click()
            return True
        except Exception as e:
            print(str(e))
            return False

    def pick_an_item(self, item_index=0, item_name=""):
        try:
            elem = self.driver.find_element_by_id(self.home_config['suggestions_id'])
            elems = elem.find_elements_by_xpath("./div")
            if item_name == "":
                elems.__getitem__(item_index).click()
            else:
                pass
                # for i, el in enumerate(elems):
            return True
        except Exception as e:
            print(str(e))
            return False
