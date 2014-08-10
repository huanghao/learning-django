from django.test import TestCase, LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


def a_very_complex_logic(a, b):
    return a * 2 + b


class SimpleTest(TestCase):

    def test_the_very_complex_logic(self):
        self.assertEquals(
            3,
            a_very_complex_logic(1, 1))


class WebTest(LiveServerTestCase):

    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()
        super(WebTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super(WebTest, cls).tearDownClass()

    def test_login(self):
        dr = self.driver
        dr.get('%s%s' % (self.live_server_url, '/accounts/login/'))

        username_input = dr.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = dr.find_element_by_name("password")
        password_input.send_keys('admin')

        dr.find_element_by_xpath('//input[@value="Login"]').click()
