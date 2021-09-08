import os

from py.xml import html
from selenium import webdriver
import pytest
from datetime import datetime
import sys
from pathlib import Path
# module_path = os.path.abspath(os.getcwd())
# module_path = Path(module_path).parent
# if str(module_path) not in sys.path:
#     sys.path.append(module_path)

from tests.functional_tests.pages.login import Login

from tests.functional_tests.fixtures.excel_utility import Excel_Utility


def pytest_addoption(parser):
    parser.addoption("--url", default="https://www.amazon.co.in")
    parser.addoption("--un", default="joy@gmail.com")
    parser.addoption("--pwd", default="joy1234")
    parser.addoption("--browser", default="local")
    parser.addoption("--env", default="prd")
    parser.addoption("--report_home", default="Directory")


@pytest.fixture(scope="session", autouse=True)
def set_attributes(request):
    session = request.node
    pytest.env = request.config.getoption("--env")
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "URL", request.config.getoption("--url"))
        setattr(cls.obj, "UN", request.config.getoption("--un"))
        setattr(cls.obj, "BrowserType", request.config.getoption("--browser"))
        setattr(cls.obj, "xls_utility", Excel_Utility("./fixtures/testdata/ecom_data.xls"))
        setattr(cls.obj, "xlsx_utility", Excel_Utility("./fixtures/testdata/ecom_data.xlsx"))

        setattr(cls.obj, "master_data_sheet", Excel_Utility("./fixtures/testdata/master_data.xlsx"))

    # request.cls.excel_utility = Excel_Utility("./fixtures/testdata/ecom_data.xlsx")
    # FOR GENERATING BUILD ID - will do later#
    date_time = datetime.now().strftime("%m-%d-%Y_%H%M%S")
    print("date and time:", date_time)


# @pytest.fixture(scope="class", autouse=True)
# def set_test_data_utility(request):
#     setattr(request.cls, "xls_utility", Excel_Utility("./fixtures/testdata/ecom_data.xls"))
#     setattr(request.cls, "xlsx_utility", Excel_Utility("./fixtures/testdata/ecom_data.xlsx"))

@pytest.fixture(scope="class", autouse=True)
def get_driver(request):
    print("==")
    request.cls.driver = None
    request.cls.env = request.config.getoption("--env")
    request.cls.uid = request.config.getoption("--un")
    request.cls.pwd = request.config.getoption("--pwd")
    request.cls.url = request.config.getoption("--url")
    chrome_options = webdriver.ChromeOptions()
    if "win" in sys.platform:
        current_date_time = datetime.now()
        curr_date_tie_str = current_date_time.strftime('%Y%m%d_%H%M%S')

        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--start-maximized')
        request.cls.driver = webdriver.Chrome(chrome_options=chrome_options)
    elif 'linux' in sys.platform:
        pass
    request.cls.driver.implicitly_wait(20)
    login_page = Login(request.cls.driver, request.cls.url, request.cls.uid, request.cls.pwd)
    request.cls.browser = login_page.launch_app()
    # request.cls.driver.get(request.cls.url)
    print("-----Execution of " + request.node.name + " has started--------")
    yield request.cls.driver
    print("-----Execution of " + request.node.name + " has stopped--------")
    request.cls.driver.quit()
    # teardown


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    timestamp = datetime.now().strftime('%H-%M-%S')

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('get_driver')
        # always add url to report

        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver.save_screenshot('./screenshots/' + timestamp + '.png')
            extra.append(pytest_html.extras.url('./screenshots/' + timestamp + '.png'))
            # only add additional html on failure
            extra.append(pytest_html.extras.image('./screenshots/' + timestamp + '.png'))
            # extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra

# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(0, html.th('TC_ID'))
#     cells.insert(0, html.th('TC_Data'))
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(cells):
#     cells.insert(0, html.td('10'))
#     cells.insert(0, html.td('this is test data'))
