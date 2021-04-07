
import unittest

import pytest

from pages.loginPage.MystoreContact import MystoreContact
from pages.loginPage.MystoreHomePage import MystoreHomePage
from pages.loginPage.MystoresignPage import MystoresignPage
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("setupmystore")
class checkouTests(unittest.TestCase):

    # it will be instantiated before other fixtures within the same scope.
    @pytest.fixture(autouse=True) #
    def objectSetup(self):
        self.loginPage = MystoresignPage(self.driver)
        self.homePage = MystoreHomePage(self.driver)
        self.contact = MystoreContact(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_verifyLinks(self):
        mainPage = self.homePage.verifyProductFooter()  # main page support list getProduct list
        self.contact.clickOnContact()
        page1 = self.contact.getProductFooter()  # page 2 get list
        result = self.contact.verifySupportList(mainPage, page1)  # get both list and validate
        self.ts.markFinal("test_checkout", result, "Checkout Verification")

    @pytest.mark.run(order=1)
    def test_verifyLinks2(self, setupmystore):
        mainPage = self.homePage.verifyProductFooter()  # main page support list getProduct list
        self.contact.clickOnContact()
        page1 = self.contact.getProductFooter()  # page 2 get list
        result = self.contact.verifySupportList(mainPage, page1)  # get both list and validate
        self.ts.markFinal("test_checkout", result, "Checkout Verification")