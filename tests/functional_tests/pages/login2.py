from selenium.webdriver.common.by import By
from tests.functional_tests.pages.base_class import base_class


class Login(base_class):

    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "")

    def __init__(self, driver, url, uid, pwd):
        base_class.__init__(self)
        self.url = url
        self.uid = uid
        self.pwd = pwd
        self.driver = driver
        self.config = self.get_config('common')
        print("==")

    def load(self):
        self.driver.get(self.url)

    def login(self):
        self.driver.get(self.url)

        ## Dummmy code - pls change it later
        self.driver.find_element_by_id(self.config['search_text_box_id']).send_keys("Samsung")

        #Write code to put user credential

        # Write code to login

        #Code to cehck logged in successfully or not

        return self.driver