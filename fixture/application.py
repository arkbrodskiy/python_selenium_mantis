from selenium import webdriver

from fixture.james import JamesHelper
from fixture.project import ProjectHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, config):
        if browser == 'firefox':
            self.wd = webdriver.Firefox(capabilities={"marionette": False},
                                        firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe")
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.base_url = config['web']['base_url']
        self.config = config
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
