from asyncio.log import logger
from lib2to3.pgen2 import driver
import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen() # Logger
    
    @pytest.mark.regression
    def test_SearchCustomerByEmail(self,setup):
        self.logger.info("******** SearchCustomerByEmail_004 ********")
        self.driver=driver
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successful ********")
        
        self.logger.info("****** Starting Search Customer By Email ******")
        
        self.logger.info("***** Seaching customer by emailID *****")
        searchcust=SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("***** TC_SearchCustomerByEmail_004 Finished *****")
        self.driver.close()