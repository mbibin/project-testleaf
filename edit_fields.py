import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class OpenHomePage:
    def home_page(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get("http://www.leafground.com/home.html")
        driver.maximize_window()
        time.sleep(2)
        url = "pages/Edit.html"
        driver.find_element(By.XPATH, '//a[@href="'+url+'"]').click()
        time.sleep(2)
        driver.find_element(By.ID, "email").send_keys("demotestfield@mail.com")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@value='Append ']").send_keys(" TestLeaf")
        time.sleep(2)
        defaultvalue = driver.find_element(By.XPATH, "//input[@value='TestLeaf']").get_attribute("value")
        print(defaultvalue)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@value='Clear me!!']").clear()
        time.sleep(2)
        isdisplayed = driver.find_element(By.XPATH, "//input[@disabled='true']").is_enabled()
        print(isdisplayed)
        time.sleep(2)

run = OpenHomePage()
run.home_page()