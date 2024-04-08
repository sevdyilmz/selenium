from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Test_Sauce:
    def web_site(self):
        driver =webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        return driver
    
    def test_null_value(self):
        driver=self.web_site()
        loginButton=driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        errorMessage= driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage.text)

    def test_null_password(self):
        driver=self.web_site()
        userName=driver.find_element(By.ID,"user-name")
        sleep(2)
        userName.send_keys("standard_user")
        sleep(2)
        loginButton=driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        errorMessage= driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage.text)
    
    def test_locked(self):
        driver=self.web_site()
        userName=driver.find_element(By.ID,"user-name")
        password=driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        sleep(2)
        loginButton=driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        errorMessage= driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage.text)
   
    def test_pro_list(self):
        driver=self.web_site()
        userName=driver.find_element(By.ID,"user-name")
        password=driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("standard_user")
        password.send_keys("secret_sauce")
        sleep(2)
        loginButton=driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(3)
        driver.get("https://www.saucedemo.com/inventory.html")
        proList=driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"sitede {len(proList)} adet ürün var.")

    

testClass=Test_Sauce()
testClass.test_null_value()
testClass.test_null_password()
testClass.test_locked()
testClass.test_pro_list()