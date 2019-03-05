from selenium import webdriver


class SwdMain:

    def __init__(self):
        self.driver_location = "/Users/burnsaustin145/PycharmProjects/SWD_2/venv/bin/chromedriver"
        self.driver = webdriver.Chrome(self.driver_location)
        self.driver.get("https://users.wix.com/signin")
        self.user = self.driver.find_element_by_name('email')
        self.password = self.driver.find_element_by_name('password')
        self.login = self.driver.find_element_by_name('submit')
        self.quit_flag = True
