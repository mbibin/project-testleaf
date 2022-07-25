from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DifferentButtons:
    def button_types(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get("http://www.leafground.com/home.html")
        driver.maximize_window()

        url = "pages/Button.html"
        driver.find_element(By.XPATH, '//a[@href="'+url+'"]').click()

        driver.find_element(By.ID, "home").click()
        driver.back()

        location = driver.find_element(By.ID, "position").location
        print(location)

        rgb = driver.find_element(By.ID, "color").value_of_css_property("background-color")
        print(rgb)

        size = driver.find_element(By.ID, "size").size
        print(size)


run = DifferentButtons()
run.button_types()