class BasePage:
    def __init__(self, driver, url):
        self.chrome = driver
        self.url = url
        self.chrome.implicitly_wait(5)
        self.chrome.maximize_window()

    def open(self):
        self.chrome.get(self.url)




