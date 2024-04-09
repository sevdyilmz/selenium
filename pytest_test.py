from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #işgili driver'ı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
import pytest



class Test_Demo:
     def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    
   
     def teardown_method(self):
        self.driver.quit()
    
     def getData():
        return [("1","1"),("abc","123"),("deneme","secret_sauce")]

     @pytest.mark.parametrize("username, password", getData())
     def test_invalid_login(self, username, password):
        userNameInput=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"password"))) 
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"login-button")))  
        loginButton.click()
        errorMessage=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))  
        assert errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
    
     def getData():
        return [("1","1"),("abc","123"),("deneme","secret_sauce")]

     @pytest.mark.parametrize("username, password", getData())
     def test_valid_login(self,username,password):
        self.driver.get("https://www.saucedemo.com/")
        userNameInput=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"user-name")))       
        passwordInput=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"password")))     
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,"login-button")))      
        loginButton.click()

        baslik=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='header_container']/div[1]/div[2]/div")))
        assert baslik.text=="Swag Labs"
        
