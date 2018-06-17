from selenium import webdriver
from pages.start_matter_main_page import StartMatterMainPage

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.start_matter_main_page = StartMatterMainPage(self.driver)

    def quit(self):
        self.driver.quit()

    def request_new_project(self, customer):
        self.start_matter_main_page.open()
        if customer.project == 'mobile':
            self.start_matter_main_page.mobileproject_radiobutton.click()
        if customer.project == 'web':
            self.start_matter_main_page.webproject_radiobutton.click()
        if customer.project == 'other':
            self.start_matter_main_page.otherproject_radiobutton.click()
        if customer.kindproject == 'hourly':
            self.start_matter_main_page.hourlykindproject_radiobutton.click()
        if customer.kindproject == 'hire':
            self.start_matter_main_page.hirekindproject_radiobutton.click()
        if customer.kindproject == 'fixed':
            self.start_matter_main_page.fixedkindproject_radiobutton.click()
        if customer.kindproject == 'fixed':
            self.start_matter_main_page.fixedkindproject_radiobutton.click()
        if customer.kindproject == 'not_sure':
            self.start_matter_main_page.notsurekindproject_radiobutton.click()
        self.start_matter_main_page.name_input.send_keys(customer.name)
        self.start_matter_main_page.email_input.send_keys(customer.email)
        self.start_matter_main_page.country_input.send_keys(customer.country)
        self.start_matter_main_page.contact_input.send_keys(customer.number)
