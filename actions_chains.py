
#action neden kullanılır? -bir element üzerinde çokça işlem yapmamız gerekirse ya da aynı işlemleri birden çok kez yapmamaız gereken yer varsa o zaman kullanılır.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #işgili driver'ı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains

class Test_Sauce:
    def __init__(self):
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
     
    
    def test_null_value(self):
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        errorMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        testResult=errorMessage.text== "Epic sadface: Username is required"
        print(f"1.Test Sonucu: {testResult}")

    def test_null_password(self):
        self.driver.get("https://www.saucedemo.com/")
        userName=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userName, "standard_user")
        actions.perform()  #depoladığım aksiyonlar
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        errorMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        testResult2=errorMessage.text=="Epic sadface: Password is required"
        print(f"2.Test Sonucu: {testResult2}")
    
    def test_locked(self):
        self.driver.get("https://www.saucedemo.com/")
        userName=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        password=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userName, "locked_out_user")
        actions.send_keys_to_element(password, "secret_sauce")
        actions.perform()
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        errorMessage= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        testResult3=errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"3.Test Sonucu: {testResult3}")
   
    def test_pro_list(self):
        self.driver.get("https://www.saucedemo.com/")
        userName=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) 
        password=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userName,"standard_user")
        actions.send_keys_to_element(password,"secret_sauce")
        actions.perform()
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "login-button")))
        loginButton.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        proList=WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.CLASS_NAME,"inventory_item")))
        print(f"Bu sitede {len(proList)} adet ürün var.")

    

testClass=Test_Sauce()
testClass.test_null_value()
testClass.test_null_password()
testClass.test_locked()
testClass.test_pro_list()