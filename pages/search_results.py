__author__ = "sarvesh.singh"

from base.common import dict_to_ns
from base.logger import Logger


class SearchResults:
    """
    Class for contains methods of Search Results Page
    """

    def __init__(self, web_driver):
        """
        To Initialize the locators of Search Results page
        :param web_driver
        """
        self.webDriver = web_driver
        self.locators = dict_to_ns({
            "results": "//*[@class='android.widget.ScrollView']/android.view.ViewGroup/android.view.ViewGroup",
            "resultsName": "//*[@class='android.widget.ScrollView']/android.view.ViewGroup/android.view.ViewGroup[%s]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]",
            "resultsPrice": "//*[@class='android.widget.ScrollView']/android.view.ViewGroup/android.view.ViewGroup[%s]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[3]",
            "searchResultsPage": "//*[@text='Filter']",
            "locationPopup": "com.flipkart.android:id/permission_title",
            "notNow": "com.flipkart.android:id/not_now_button",
        })
        self.logger = Logger(name="RESULTS").get_logger

    def close_location_pop_up(self):
        """
        Close the location popup
        :return:
        """
        self.webDriver.explicit_visibility_of_element(element=self.locators.locationPopup, locator_type='id',
                                                      time_out=60)
        self.webDriver.click(element=self.locators.notNow, locator_type='id')

    def print_search_results(self):
        """
        print the search results in console
        :return:
        """
        self.webDriver.explicit_visibility_of_element(element=self.locators.searchResultsPage, locator_type='xpath',
                                                      time_out=60)
        results = self.webDriver.get_elements(element=self.locators.results, locator_type='xpath')
        for _result in results:
            index = results.index(_result) + 2
            if index > len(results):
                break
            name = self.webDriver.get_text(element=self.locators.resultsName % index, locator_type='xpath')
            price = self.webDriver.get_text(element=self.locators.resultsPrice % index, locator_type='xpath')
            self.logger.info(f'Device Name - {name} | Price - {price}')
