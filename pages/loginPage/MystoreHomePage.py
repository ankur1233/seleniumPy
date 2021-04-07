from collections import defaultdict

import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
import random

from utilities.util import Util

amt = ""


class MystoreHomePage(BasePage):
    # global
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()



    # locaotr
    popularproduct = "#homefeatured .left-block .product-image-container"
    _popularproductAddCart = '#homefeatured .product-container .button-container a'

    test1 = "//a[text()='Selenium Framework']"
    _totalproduct = ".ajax_block_products_total"
    _totlashipping = "span[class='ajax_cart_shipping_cost']"
    _totalamunt = "span[class='ajax_block_cart_total']"

    _createEmail = "email_create"
    _createEmailBtn = "SubmitCreate"

    _checkout = "a[title='Proceed to checkout']"
    checkout = "(//a[@title='Proceed to checkout'] )[2]"

    productheadre = "//h4[text()='Information']"

    productList = "//h4[text()='Information']/following-sibling::ul/li/a"

    def getProduct(self):
        return self.getText(self.productheadre,locatorType="xpath")

    def getProductList(self):
        return self.getElementList(self.productList,locatorType="xpath")

    def test(self):
        #self.webScroll(self.test1)
        self.elementClick(self.test1,locatorType="xpath")

    def verifyProductFooter(self):
        d = []
        e = ['Informatio', 'Specials', 'New products', 'Best sellers', 'Our stores', 'Contact us', 'Terms and conditions of use', 'About us', 'Sitemap']
        product = self.getProduct()
        productlist = self.getProductList()
        d.append(product)
        #d = defaultdict(list)

        #d.keys(product)
        for plist in productlist:
            txt = self.getText(element=plist)
            #d[product].append(txt)
            d.append(txt)

        if d == e:
            self.log.info("List are equal")
        else:
            self.log.info("list are not equal")
            #print(self.getText(element=plist))
        self.log.info(d)
        #self.log.info(d.keys())

        assert True
        return d

    def selectProduct(self):
        elements = self.getElementList(self.popularproduct, locatorType="css")
        for idx, ele in enumerate(elements):
            if idx == 0:
                self.getActionDriver().move_to_element(ele).perform()
                break

    # def popularProduct(self):
    #     self.getActionDriver().move_to_element(self.driver.find_element_by_id('_popularproduct')).perform()

    def addToCart(self):
        self.waitForElement(self._popularproductAddCart, locatorType="css")
        elements = self.getElementList(self._popularproductAddCart, locatorType="css")
        for idx, ele in enumerate(elements):
            if idx == 0:
                self.elementClick(element=ele)
                break

    def verifyTotalCost(self):
        self.waitForElement(self._totalamunt, locatorType="css")
        product_amt = self.getText(self._totalproduct, locatorType="css")
        shiping_amt = self.getText(self._totlashipping, locatorType="css")
        total_amt = self.getText(self._totalamunt, locatorType="css")
        amt = float(product_amt.replace("$", "").strip()) + float(shiping_amt.replace("$", "").strip())
        # verify ammount
        self.util.verifyTextMatch(str(amt), total_amt.replace("$", "").strip())
        # self.amt = amt
        self.setamt(amt)

    def setamt(self,amt):
        global amt1
        amt1=amt

    def getAmout(self):
        return amt1

    def clickOnCheckoutLink(self):
        self.elementClick(self._checkout, locatorType="css")

    def clickOncheckout(self):
        self.elementClick(self.checkout, locatorType="xpath")

    def getEmail(self):
        self.sendKeys(str("abcb" + str(random.randint(1, 100)) + "@gmail.com"), self._createEmail)

    def createEmail(self):
        self.elementClick(self._createEmailBtn)
