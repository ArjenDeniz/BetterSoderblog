from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager

#loads the driver and waits for it to load
driver = webdriver.Firefox(GeckoDriverManager().install())
driver = webdriver.Firefox()
driver.implicitly_wait(2)

driver.get("https://extension765.com/blogs/soderblog/seen-read-2023")

#takes the text from the post_main class
text = driver.find_element(By.ID,"post_main").text
print(text)

#exits the driver
driver.close()