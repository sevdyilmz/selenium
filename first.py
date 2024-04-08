from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

sleep(3)

input = driver.find_element(By.NAME, "q")
input.send_keys("kodlama.io")
sleep(3)

searchButton = driver.find_element(By.NAME, "btnK")
sleep(2)
searchButton.click()
sleep(5)

button =driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
sleep(2)
button.click()
sleep(3)

howMany=driver.find_elements(By.CLASS_NAME, "course-listing")
print(f"kodlama.io sitesinde şu anda {len(howMany)} tane kurs vardır.")
sleep(5)





# while True:
#     continue
