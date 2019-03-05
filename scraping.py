from selenium import webdriver
import pprint


class Scrape:

    def __init__(self):
        self.driver_location = "/Users/burnsaustin145/python_projects/analogy_machine/lib/chromedriver"
        self.driver = webdriver.Chrome(self.driver_location)
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
        self.driver.implicitly_wait(10)
        self.article_dict = {}
        self.quit_flag = True

    def random_get(self):
        """gets random articles"""
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
        self.driver.implicitly_wait(10)
        random_article = self.driver.find_element_by_css_selector('#n-randompage > a')
        random_article.click()
        self.driver.implicitly_wait(10)
        curr_article = self.driver.current_url

        return curr_article

    def random_scrape(self):
        """composes random_get"""

        curr_article = self.random_get()
        print("curr_article = " + curr_article)
        curr_element = self.driver.find_element_by_class_name("mw-parser-output")
        self.driver.implicitly_wait(10)
        print(curr_element)
        text = curr_element.text
        print(curr_article, text)
        return text

    def random_composition(self, n):
        """iterates random scrape 'n' times and saves
        results to dict"""

        for foo in range(n):
            self.article_dict[foo] = self.random_scrape()

    def get_article_dict(self):
        pprint.pprint(self.article_dict)


scrape = Scrape()
scrape.random_composition(50)
scrape.get_article_dict()






