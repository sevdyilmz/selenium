from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #işgili driver'ı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pytest

class Test_Pytest:
    def setup_method(self):
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
     
    def teardown_method(self):
        self.driver.quit()

    def test_null_login(self):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"")
        actions.send_keys_to_element(passwordInput,"")
        actions.click(loginButton)
        actions.perform() 
        errorMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text=="Epic sadface: Username is required"
    
    def test_null_password_login(self):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"Ayşe")
        actions.send_keys_to_element(passwordInput,"")
        actions.click(loginButton)
        actions.perform() 
        errorMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text=="Epic sadface: Password is required" 
        

    def test_lockedUser_login(self):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"locked_out_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.click(loginButton)
        actions.perform() 
        errorMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text=="Epic sadface: Sorry, this user has been locked out."

    def test_valid_login(self):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.click(loginButton)
        actions.perform()
        baslik=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//div[@class='app_logo']")))
        assert baslik.text=="Swag Labs"
        listOfProducts=self.driver.find_elements(By.CSS_SELECTOR,"div[class='inventory_item']")
        print(len(listOfProducts))
        assert len(listOfProducts)==6
    
    
    def getData():
        return [("sevda","1071"),("yılmaz","253"),("Nur ebrar","secret_sauce")]
    
    @pytest.mark.parametrize("username,password",getData())  
    def test_invalid_login(self,username,password):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.click(loginButton)
        actions.perform()
        errorMesssage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMesssage.text=="Epic sadface: Username and password do not match any user in this service"
   
    def test_addProduct(self):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.click(loginButton)
        actions.perform()
        product=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"add-to-cart-sauce-labs-bike-light")))
        product.click()
        addToCart=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-onesi']")))
        cart_button_text=addToCart.text
        print("Cart Button Text:", cart_button_text)
        assert addToCart.text=="1"