from selenium.webdriver.support.wait import WebDriverWait

class StartMatterMainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://startmatter.com/")
        return self

    @property
    def mobileproject_radiobutton(self):
        return self.driver.find_element_by_css_selector("label[for=mobile]")

    @property
    def webproject_radiobutton(self):
        return self.driver.find_element_by_css_selector("label[for=web]")

    @property
    def otherproject_radiobutton(self):
        return self.driver.find_element_by_css_selector("label[for=other]")

    @property
    def hourlykindproject_radiobutton(self):
        return self.driver.find_element_by_css_selector("label[for=hourly]")

    @property
    def hirekindproject_radiobutton(self):
        return self.driver.find_element_by_css_selector("label[for=hire]")

    @property
    def notsurekindproject_radiobutton(self):
        return self.driver.find_element_by_css_selector("label[for=not_sure]")

    @property
    def fixedkindproject_radiobutton(self):
        return self.driver.find_element_by_css_selector("label[for=fixed]")

    @property
    def name_input(self):
        return self.driver.find_element_by_id("name")

    @property
    def email_input(self):
        return self.driver.find_element_by_id("email")

    @property
    def country_input(self):
        return self.driver.find_element_by_id("country")

    @property
    def contact_input(self):
        return self.driver.find_element_by_id("contact")

    @property
    def sendrequest_button(self):
        return self.driver.find_element_by_css_selector("input.button-default.button-default_md_mobile")
