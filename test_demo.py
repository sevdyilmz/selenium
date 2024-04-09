from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep




class Test_Sauce:
    def test_invalid_login(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginBtn=driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"test sonucu1:{testResult}")
   
    def test_null_userName(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        passwordInput=driver.find_element(By.ID, "password")
        sleep(2)
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult1=errorMessage.text=="Epic sadface: Username is required"
        print(f"test sonucu2:{testResult1}")
    
    def test_null_password(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput=driver.find_element(By.ID, "user-name")
        sleep(2)
        usernameInput.send_keys("standard_user")
        sleep(2)
        loginBtn=driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult2=errorMessage.text=="Epic sadface: Password is required"
        print(f"test sonucu3:{testResult2}")
    
    def test_locked_user(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult4=errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"test sonucu4:{testResult4}")
    
    def test_valid_login(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        baslık=driver.find_element(By.XPATH,"//*[@id='header_container']/div[1]/div[2]/div")
        testResult5=baslık.text=="Swag Labs"
        print(f"test sonucu5:{testResult5}")
    
    def test_add_Product(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        addToCart=driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie")
        addToCart.click()
        check=driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a/span")
        testResult6=check.text=="1"
        print(f"test sonucu6:{testResult6}")
    
    def test_remove_Product(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.XPATH,"//*[@id='login-button']")
        sleep(2) 
        loginBtn.click()
        sleep(2)
        addToCart=driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie")
        addToCart.click()
        remove=driver.find_element(By.ID,"remove-sauce-labs-onesie")
        remove.click()
        check1=driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie")
        testResult7=check1.text=="Add to cart"
        print(f"test sonucu7:{testResult7}")


testClass=Test_Sauce()
testClass.test_invalid_login()
testClass.test_null_userName()
testClass.test_null_password()
testClass.test_locked_user()
testClass.test_valid_login()
testClass.test_add_Product()
testClass.test_remove_Product()



    