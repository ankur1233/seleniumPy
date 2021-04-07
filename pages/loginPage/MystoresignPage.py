import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.loginPage.MystoreHomePage import MystoreHomePage
from utilities.util import Util


class MystoresignPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()
        #self.log=MystoreHomePage(driver)

    # locator
    _title = ".radio-inline label div"
    _firstName = "customer_firstname"
    _lastName = "customer_lastname"
    _pass = "passwd"
    _city = "city"
    _state = "id_state"
    _phone = "phone_mobile"
    _address = "address1"
    _postal = "postcode"

    _register = "submitAccount"

    _processAddress = "button[name='processAddress']"

    _checkbox = ".checker"
    _processCarrier = "button[name='processCarrier']"

    _payment = ".bankwire"

    _confirmOrder = "//span[text()='I confirm my order']"

    _totalammountfinal = ".price strong"

    checkout = "(//a[@title='Proceed to checkout'] )[2]"

    def clickOnCheckoutLink(self):
        self.elementClick(self.checkout, locatorType="css")

    def registerUser(self):
        self.waitForElement(self._firstName)
        eleList = self.getElementList(self._title, locatorType="css")
        for idx, ele in enumerate(eleList):
            if idx == 0:
                self.elementClick(element=ele)
                break
        self.sendKeys("test", self._firstName)
        self.sendKeys("User", self._lastName)
        self.sendKeys("password123", self._pass)
        self.sendKeys("city", self._city)
        self.selectByText("Alaska", self._state)
        self.sendKeys("12454545", self._phone)
        self.sendKeys("abb121aa", self._address)
        self.sendKeys("00005", self._postal)
        self.elementClick(self._register)

    def clickOnProceed(self):
        self.elementClick(self.checkout, locatorType="xpath")

    def clickOnProceedAddress(self):
        self.waitForElement(self._processAddress, locatorType="css")
        self.elementClick(self._processAddress, locatorType="css")

    def clickOnProceedCarrier(self):
        self.waitForElement(self._processCarrier, locatorType="css")
        self.elementClick(self._processCarrier, locatorType="css")

    def clickOnTerms(self):
        self.elementClick(self._checkbox, locatorType="css")

    def pay(self):
        self.waitForElement(self._payment, locatorType="css")
        self.elementClick(self._payment, locatorType="css")

    def confirmOrder(self):
        self.elementClick(self._confirmOrder, locatorType="xpath")

    def verifyAmt(self,amt11):
        final = self.getText(self._totalammountfinal, locatorType="css")
        n = amt11
        self.util.verifyTextMatch(final.replace("$", "").strip(),amt11)
