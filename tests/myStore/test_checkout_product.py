from pages.loginPage.MystoreContact import MystoreContact
from pages.loginPage.MystoreHomePage import MystoreHomePage
from pages.loginPage.MystoresignPage import MystoresignPage
import unittest
import pytest

#from tests.conftest import getUser, getPassword
from tests.conftest import setupmystore
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("setupmystore", "user", "password")
class checkoutProductTests(unittest.TestCase):
    """Product check out """

    # it will be instantiated before other fixtures within the same scope.
    @pytest.fixture(autouse=True)  #
    def objectSetup(self,setupmystore):
        self.loginPage = MystoresignPage(self.driver)
        self.homePage = MystoreHomePage(self.driver)
        self.contact = MystoreContact(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_checkout(self):
        """check out"""
        self.homePage.selectProduct()
        self.homePage.addToCart()
        self.homePage.verifyTotalCost()  # validation spoint
        self.homePage.clickOnCheckoutLink()
        self.homePage.clickOncheckout()
        self.homePage.getEmail()
        self.homePage.createEmail()
        self.loginPage.registerUser()
        self.loginPage.clickOnProceedAddress()
        self.loginPage.clickOnTerms()
        self.loginPage.clickOnProceedCarrier()
        self.loginPage.pay()
        self.loginPage.confirmOrder()
        self.ts.markFinal("test_checkout", True, "Checkout Verification")
        self.loginPage.verifyAmt(self.homePage.getAmout()) # validation pointas

    # @pytest.mark.run(order=1)
    # def test_verifyLinks(self):
    #     """verify links"""
    #     # print("User Name:: "+getUser())
    #     # print("Password User :: "+str(getPassword()))
    #     mainPage = self.homePage.verifyProductFooter()  # main page support list getProduct list
    #     print("Test")
    #     # self.contact.clickOnContact()checkoutProductTests
    #     # self.homePage.webScroll(self.test)
    #     # self.homePage.test()
    #     # self.homePage.elementClick(self)
    #     # self.homePage.elementClickJS()
    #     # self.contact.clickOnContact()
    #     # page1 = self.contact.getProductFooter()  # page 2 get list
    #     # result = self.contact.verifySupportList(mainPage, page1)  # get both list and validate
    #     # self.ts.markFinal("test_checkout", result, "Checkout Verification")
    #     assert False

    @pytest.mark.run(order=2)
    def test_verifytest1(self):
            """verify Prosuct 1"""
            print("Pass :: Product 1")
            assert True

    @pytest.mark.run(order=3)
    def test_verifytest2(self):
        """verify Product 2"""
        print("Pass :: Product 2")
        assert True

    @pytest.mark.run(order=4)
    def test_verifytest3(self):
        print("Pass :: Product 1")
        """verify Product 3"""
        assert True
