import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class DynamicContentPage:
    URL = 'https://the-internet.herokuapp.com/dynamic_content'
    paragraph_one_css_selector = '#content > div:nth-child(1) > div.large-10.columns'
    paragraph_two_css_selector = '#content > div:nth-child(4) > div.large-10.columns'
    paragraph_three_css_selector = '#content > div:nth-child(7) > div.large-10.columns'

    image_one_css_selector = '#content > div:nth-child(1) > div.large-2.columns > img'
    image_two_css_selector = '#content > div:nth-child(4) > div.large-2.columns > img'
    image_three_css_selector = '#content > div:nth-child(7) > div.large-2.columns > img'

    def __init__(self, browser):
        self.browser = browser
    
    def load(self):
        self.browser.get(self.URL)
    
    def get_paragraph_one_text(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.paragraph_one_css_selector).text
    
    def get_paragraph_two_text(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.paragraph_two_css_selector).text

    def get_paragraph_three_text(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.paragraph_three_css_selector).text

    def get_image_one(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.image_one_css_selector).text
        
    def get_image_two(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.image_two_css_selector).text

    def get_image_three(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.image_three_css_selector).text