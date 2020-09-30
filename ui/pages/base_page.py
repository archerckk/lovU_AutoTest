import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def _find(self, by, locator=None):
        # 兼容元组跟多元素传入

        element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)

        return element

    def steps(self, path, key,name=None):
        with open(path)as f:
            steps: list = yaml.safe_load(f)[key]
        element = None
        for step in steps:
            if 'by' in step.keys():
                element = self._find(step['by'], step['locator'])
                if 'action' in step.keys():
                    action = step['action']
                    if action == 'click':
                        element.click()

    def _finds(self, by, locator=None):
        # 兼容元组跟多元素传入

        elements = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_elements(by, locator)

        return elements

    def _find_focus(self, by):
        # element = WebDriverWait(self._driver, 25).until(expected_conditions.presence_of_element_located(by)) if \
        #     isinstance(by, tuple) else WebDriverWait(self._driver, 25).until(
        #     expected_conditions.presence_of_element_located((by, locator)))
        # return element
        return WebDriverWait(self._driver, 40).until(expected_conditions.presence_of_element_located(by))

    def _finds_focus(self, by):
        return WebDriverWait(self._driver, 40).until(expected_conditions.visibility_of_all_elements_located(by))


    def _wait_disappear(self,by):
        return WebDriverWait(self._driver,40).until_not(expected_conditions.presence_of_all_elements_located(by))

    def confirm_element_disappear(self, by, locator=None):
        # 确认元素删除成功

        element = WebDriverWait(self._driver, 15).until_not(expected_conditions.presence_of_element_located(by)) if \
            isinstance(by, tuple) else WebDriverWait(self._driver, 15).until_not(
            expected_conditions.presence_of_element_located((by, locator)))
        return element

    def back(self, num=1):
        for i in range(num):
            self._driver.back()

    def scroll_find(self, text):
        element = self._driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).'
            f'instance(0)).scrollIntoView(new UiSelector().text("{text}").'
            f'instance(0));')
        return element

    def _find_and_click(self, by):
        self._find(by).click()

    def get_toast(self):
        return self._find_focus((By.XPATH, '//*[@class="android.widget.Toast"]')).text
