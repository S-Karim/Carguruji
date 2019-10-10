import unittest
from selenium import webdriver
import time
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from POM1.REGISTRATION1.signup import Signup_page
from POM1.REGISTRATION1.REGISTRATION1 import RegistrationPage
from POM1.REGISTRATION1.login import Loginpage
from POM1.CART1.ADDTOCAR1 import AddItemCart
from POM1.SCREENSHOT1 import SCREENSHT2
from POM import report

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/akkar/PycharmProjects/sobiasif/POM/Driver/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        print("Test Start")

    def test1_sign_up1(self):
        driver = self.driver
        driver.get("http://carguruji.com/shop/login?back=my-account")
        driver.implicitly_wait(20)
        signup = Signup_page(driver)
        signup.click_sign_in()
        signup.enter_email("caccatesting123@gmail.com")
        signup.click_create_account()
        driver.implicitly_wait(5)
        reg = RegistrationPage(driver)
        reg.click_title_Mrs()
        reg.enter_firstname("sk")
        reg.enter_lastname("Ali")
        reg.enter_email("")
        reg.enter_password("Skali2019*")
        reg.select_day()
        reg.select_month()
        reg.select_year()
        reg.click_register()

    def test2_sign_in2(self):
        driver = self.driver
        driver.get("http://carguruji.com/shop/login?back=my-account")
        driver.implicitly_wait(5)
        log=Loginpage(driver)
        log.click_signin1()
        log.enter_email1("irhaali17@outlook.com")
        log.enter_password1("Skali2019*")
        log.click_Signin2()
        driver.implicitly_wait(5)
        self.driver.get_screenshot_as_file("C:/Users/akkar/PycharmProjects/sobiasif/POM1/SCREENSHOT1.png")
        cart = AddItemCart(driver)
        cart.click_women()
        driver.implicitly_wait(5)
        cart.click_tops()
        driver.implicitly_wait(5)
        cart.click_blouses()
        driver.implicitly_wait(5)
        driver.execute_script("window.scrollBy(0,1000)", "")
        cart.click_selectblouse()
        driver.implicitly_wait(5)
        cart.click_addtocart()
        driver.implicitly_wait(5)
        cart.click_proceedcheckout1()
        driver.implicitly_wait(5)
        cart.click_proceedcheckout2()
        driver.implicitly_wait(5)
        '''cart.click_address("cacc4630")
        cart.click_city("Alaska")
        cart.click_state()
        cart.click_postalcode("99501")
        cart.click_country()
        cart.click_phonenumber("4166610888")
        cart.click_mobilenumber("4166610888")
        cart.click_save()'''
        cart.click_checkout1()
        cart.click_terms()
        cart.click_checkout2()
        driver.execute_script("window.scrollBy(0,1000)", "")
        cart.click_paybycheck()
        cart.click_confirmorder()
        self.driver.get_screenshot_as_file("C:/Users/akkar/PycharmProjects/sobiasif/POM1/SCREENSHOT1.png")

        log.click_signout()
        title = driver.title
        self.assertEqual("Login - CarGuruji Shop", title, )

        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()

    if __name__ == '__main__':
        unittest.main(testRunner=(
            HtmlTestRunner.HTMLTestRunner(output="/Users/akkar/PycharmProjects/sobiasif/POM1/REPORT1/REPORT2.py")))