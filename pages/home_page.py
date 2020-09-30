__author__ = "sarvesh.singh"

from base.common import dict_to_ns


class HomePage:
    """
    Class for contains methods of Home Page
    """

    def __init__(self, web_driver):
        """
        To Initialize the locators of Home page
        :param web_driver
        """
        self.webDriver = web_driver
        self.locators = dict_to_ns({
            "closePopUp": "com.flipkart.android:id/btn_skip",
            "searchBoxWrite": "com.flipkart.android:id/search_autoCompleteTextView",
            "searchBox": "//*[@resource-id='com.flipkart.android:id/search_widget_textbox']",
        })

    def close_pop_up(self):
        """
        Close the signup pop up
        :return:
        """
        self.webDriver.click(element=self.locators.closePopUp, locator_type='id')

    def search_apple(self):
        """
        Search Apple
        :return:
        """
        self.webDriver.explicit_visibility_of_element(element=self.locators.searchBox, locator_type='xpath',
                                                      time_out=60)
        self.webDriver.click(element=self.locators.searchBox, locator_type='xpath')
        self.webDriver.set_text(element=self.locators.searchBoxWrite, locator_type='id', text='apple')
        self.webDriver.submit()
