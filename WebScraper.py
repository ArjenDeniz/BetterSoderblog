from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

#loads the driver and waits for it to load
driver = webdriver.Firefox()
driver.implicitly_wait(2)

driver.get("https://extension765.com/blogs/soderblog/seen-read-2023")

#takes the html from the post_main class
main_post = driver.find_element(By.ID,"post_main")
html_version =  main_post.get_attribute('outerHTML')

soup = BeautifulSoup(html_version, 'html.parser')

#keeps the bold and italics tags for further use
def extract_text_with_tags(soup):
    for tag in soup.find_all(True): 
        if tag.name not in ['strong', 'em']:
            tag.unwrap()  
    return str(soup)


rich_text = extract_text_with_tags(soup)

print(rich_text)



#exits the driver
driver.close()