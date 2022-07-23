from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests

class HyperLinks:
    def link_types(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get("http://www.leafground.com/home.html")
        driver.maximize_window()
        url = "pages/Link.html"
        driver.find_element(By.XPATH, '//a[@href="'+url+'"]').click()
        driver.find_element(By.XPATH, '//a[@href="../home.html"]').click()
        driver.back()
        find_link = driver.find_element(By.XPATH, '//a[@href="Button.html"]').get_attribute("href")
        print(find_link)
        # request = driver.find_element(By.XPATH, '//a[@href="error.html"]').get_attribute("href")
        r = requests.head(driver.find_element(By.XPATH, '//a[@href="error.html"]').get_attribute("href"))
        print(r.status_code == 404)
        driver.find_element(By.XPATH, '//a[@href="../home.html"][1]').click()
        driver.back()
        links = driver.find_elements(By.TAG_NAME, "a")
        print(len(links))


run = HyperLinks()
run.link_types()