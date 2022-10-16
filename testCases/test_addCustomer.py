import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen() #Logger
    
    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("******** Test_003_AddCustomer ********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successful ********")
        
        self.logger.info("***** Starting Add Customer Test *****")
        
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        
        self.addcust.clickOnAddnew()
        
        self.logger.info("******** Prividing customer info ********")
        
        # self.email=random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword(self.abcd1234)
        self.addcust.setcustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("ABCD")
        self.addcust.setLastName("PQR")
        self.addcust.setDob("4/5/1991")
        self.addcust.setComapnyName("XYZ")
        self.addcust.setAdminContent("this is for testing.....")
        self.addcust.clickOnSave()
        
        self.logger.info("******** Saving customer info ********")
        
        self.logger.info("***** Add customer validation started *****")
        
        self.msg=self.driver.find_element_by_tag_name("body").text
        
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True==True
            self.logger.info("******** Add customer Test Passed ********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png") #Screenshot
            self.logger.error("******** Add customer Test Failed ********")
            assert True==False
            
        self.driver.close()
        self.logger.info("***** Ending Test_003_AddCustomer Test *****")
        
def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))