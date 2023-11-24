import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from Config.dataconfig import TestData


'''Untuk argumen tambahan saat running pytest pilih browser apa, example : pytest --browser=chrome -vs dst.... '''
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

'''Fixture untuk scope : TEST FUNCTION'''
@pytest.fixture()
def setup_scope_function(request):
    web_driver = None
    browser = request.config.getoption("browser")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # for chrome only
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")  # for chrome only
        options.add_argument("--start-maximized")
        # options.headless = True
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser == "edge":
        web_driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    web_driver.maximize_window()
    web_driver.get(TestData.BASE_URL_PROD)
    request.cls.driver = web_driver
    yield
    web_driver.quit()


'''Fixture untuk scope : TEST CLASS'''
@pytest.fixture(scope="class")
def setup_scope_class(request):
    web_driver = None
    browser = request.config.getoption("browser")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # for chrome only
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")  # for chrome only
        options.add_argument("--start-maximized")
        # options.headless = True
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser == "edge":
        web_driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    web_driver.maximize_window()
    web_driver.get(TestData.BASE_URL_UAT)
    request.cls.driver = web_driver
    yield
    web_driver.quit()
