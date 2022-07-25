from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class EditFields:
    def fields_types(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get("http://www.leafground.com/home.html")
        driver.maximize_window()

        url = "pages/Edit.html"
        driver.find_element(By.XPATH, '//a[@href="'+url+'"]').click()

        driver.find_element(By.ID, "email").send_keys("demotestfield@mail.com")

        driver.find_element(By.XPATH, "//input[@value='Append ']").send_keys(" TestLeaf")

        default_value = driver.find_element(By.XPATH, "//input[@value='TestLeaf']").get_attribute("value")
        assert default_value == "TestLeaf"

        driver.find_element(By.XPATH, "//input[@value='Clear me!!']").clear()

        is_displayed = driver.find_element(By.XPATH, "//input[@disabled='true']").is_enabled()
        assert is_displayed == False


run = EditFields()
run.fields_types()