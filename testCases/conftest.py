import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def setup(browser):
    # if browser=="chrome":
    #     # driver=webdriver.Chrome()
    #     serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver")
    #     driver=webdriver.Chrome(service=serv_obj)
    #     print("Launching Chrome browser.....")
    # elif browser=="Firefox":
    #     driver.webdriver.Firefox()
    #     print("Launching Firefox browser.....")
    # else:
    #     driver=webdriver.Ie()
    
    serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver")
    driver=webdriver.Chrome(service=serv_obj)
    return driver

def pytest_addoption(parser): #This will get the value from CLI/hooks
    parser.addoption("--browser")
    
@pytest.fixture()
def browser(request): #This will return the Browser value to setup method
    return request.config.getoption("--browser")

#Pytest HTML Report
#It is hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name']='non Commerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='ABCD'
    
#It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)  