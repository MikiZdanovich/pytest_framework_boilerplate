import os
import json

class Config:
    PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'browser_config.json')

    @staticmethod
    def set_config(browser_name):
        with open(Config.PATH, 'r') as config_file:
            browser_config = json.loads(config_file.read())

        return browser_config[browser_name]

    @staticmethod
    def set_implicity_wait_time(implicity_wait=10):
        return implicity_wait

    @staticmethod
    def set_page_load_timeout(page_load_timeout=30):
        return page_load_timeout

