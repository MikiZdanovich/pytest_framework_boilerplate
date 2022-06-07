import os


class Config:
    def __init__(self, browser_name):
        self.browser_config = {
            'chrome': ("headless", "start-maximized", "incognito", "disable-infobars", "window-size=800x600"),
            'firefox': ("start-maximized", "incognito", "disable-infobars", "window-size=800x600")
        }[browser_name]

    def get_implicity_wait_time(self):
        return os.environ.get('IMPLICITY_WAIT_TIME', '10')
