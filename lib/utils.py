import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from robot.libraries.BuiltIn import BuiltIn
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class utils:
    """
        utilities to be used across the modules
        """

    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.builtin = BuiltIn()
        self._logger = BuiltIn().log

    def login_to_ui(self, login_url, user, password):
        self.driver = webdriver.Chrome()
        self.driver.get(login_url)
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.ID, "user-name").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        assert self.driver.find_element(By.XPATH, '//span[@class="title"]').is_displayed() == True

    def add_bike_light_to_cart(self):
        # self.driver = webdriver.Chrome(options=self.option)
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
        self.driver.implicitly_wait(5)
        self.item_name_added_to_cart = self.driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
        self.driver.implicitly_wait(5)
        self.item_name_added_to_cart = self.item_name_added_to_cart.text
        # print(item_name_added_to_cart.text)
        if self.item_name_added_to_cart == "Sauce Labs Bike Light":
            print("Item added to cart successfully")
        else:
            print("Item is not to cart")
        return self.item_name_added_to_cart

    def remove_added_bike_light_to_cart(self):
        time.sleep(2)
        # self.driver.find_element(By.ID, "continue-shopping").click()
        self.driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
        var1 = self.driver.find_elements(By.XPATH, '//div[@class="cart_contents_container"]')
        for elements in var1:
            if elements.text == "Sauce Labs Bike Light":
                print("Item is not removed from cart")
            else:
                print("Item is successfully removed from cart")

    def check_out_step_one(self):
        self.driver.find_element(By.ID, 'checkout').click()
        self.driver.find_element(By.ID, 'first-name').send_keys('fname')
        self.driver.find_element(By.ID, 'last-name').send_keys('lname')
        self.driver.find_element(By.ID, 'postal-code').send_keys('111')
        self.driver.find_element(By.ID, 'continue').click()
        added_item_in_cart = self.item_name_added_to_cart
        print("Name of item added in cart is ", added_item_in_cart)
        for cart_item in self.driver.find_elements(By.XPATH, ('//div[@class="cart_item"]')):
            cart_item = cart_item.text
            new_cart_item = list(cart_item.split('\n'))
            print("fetched item from list is ", new_cart_item[1])
            if new_cart_item[1] == added_item_in_cart:
                print("added item is present in cart")
        print("checkout step one completed")

    def check_out_step_two(self):
        global new_item_price, final_tax, new_cart_price
        item_price = self.driver.find_elements(By.XPATH, '//div[@class="summary_subtotal_label"]')
        for price in item_price:  # Item price for that item wihout tax
            price = price.text
            new_item_price = list(price.split('$'))
            print(new_item_price[1])
        tax_price = self.driver.find_elements(By.XPATH, '//div[@class="summary_tax_label"]')
        for tax in tax_price:  # Tax price for the applicable item
            tax = tax.text
            final_tax = list(tax.split('$'))
            print(final_tax[1])
        final_price = float(new_item_price[1]) + float(final_tax[1])
        final_round_off_price = round(final_price, 2)
        print(final_round_off_price)

        final_price_from_cart = self.driver.find_elements(By.XPATH,
                                                          '//div[@class="summary_info_label summary_total_label"]')

        for cart_price in final_price_from_cart:  # Final frice of item
            cart_price = cart_price.text
            new_cart_price = list(cart_price.split('$'))
            print(new_cart_price[1])

        final_cart_price = float(new_cart_price[1])
        final_round_off_cart_price = round(final_cart_price, 2)
        print(final_round_off_cart_price)

        if final_round_off_price == final_round_off_price:
            print("price is correct")

    def logout_from_cart(self):
        self.driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
        self.driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]').click()
        print("Logout successfully")


if __name__ == "__main__":
    pass
