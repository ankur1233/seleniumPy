from collections import defaultdict

import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
import random

from utilities.util import Util

amt = ""


class MystoreContact(BasePage):
    # global
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    # loactor

    contactBtn = "//a[@title='Contact Us']"

    productheadre = "//h4[text()='Information']"

    productList = "//h4[text()='Information']/following-sibling::ul/li/a"

    def clickOnContact(self):
        self.elementClick(self.contactBtn, locatorType="xpath")

    def getProduct(self):
        return self.getText(self.productheadre, locatorType="xpath")

    def getProductList(self):
        return self.getElementList(self.productList, locatorType="xpath")

    def getProductFooter(self):
        d = []
        e = ['Information', 'Specials', 'New products', 'Best sellers', 'Our stores', 'Contact us',
             'Terms and conditions of use', 'About us', 'Sitemap']
        product = self.getProduct()
        productlist = self.getProductList()
        d.append(product)
        # d = defaultdict(list)

        # d.keys(product)
        for plist in productlist:
            txt = self.getText(element=plist)
            # d[product].append(txt)
            d.append(txt)

        # if d == e:
        #     self.log.info("List are equal")
        # else:
        #     self.log.info("list are not equal")
        # print(self.getText(element=plist))
        self.log.info(d)
        # self.log.info(d.keys())

        return d

    def verifySupportList(self,l1,l2):

       return self.listMatch(l1,l2)