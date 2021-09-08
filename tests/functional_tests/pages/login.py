from tests.functional_tests.pages.base_class import base_class


class Login(base_class):

    def __init__(self, driver, url, uid, pwd):
        self.url = url
        self.uid = uid
        self.pwd = pwd
        self.driver = driver
        self.config = self.get_config('common')
        print("==")

    def load(self):
        self.driver.get(self.url)

    def launch_app(self):
        self.driver.delete_all_cookies()
        self.driver.get(self.url)
        for li in self.driver.get_log('browser'):
            print(str(li))

        #Write code to put user credential
        # Write code to login
        #Code to cehck logged in successfully or not

        return self.driver