import os

from src.utils.json_parser import JsonParser


class Config:
    _browser_config_name = 'browser_config.json'
    _configs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'configs')
    json_parser = JsonParser(_browser_config_name, _configs_path)

    @staticmethod
    def set_config(browser_name):
        return Config.json_parser.read_from_json()[browser_name]

    @staticmethod
    def set_implicity_wait_time(implicity_wait=10):
        return implicity_wait

    @staticmethod
    def set_page_load_timeout(page_load_timeout=30):
        return page_load_timeout
