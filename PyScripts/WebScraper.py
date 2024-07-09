from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os

#keeps the bold and italics tags for further use
def Extract_Text_With_Tags(soup):
    for tag in soup.find_all(True): 
        if tag.name not in ['strong', 'em']:
            tag.unwrap()  
    return str(soup)

def Link_To_Text(year):
    driver = webdriver.Firefox()
    driver.implicitly_wait(2)
    driver.get('https://extension765.com/blogs/soderblog/seen-read-' + str(year))
    #takes the html from the post_main class
    main_post = driver.find_element(By.ID,"post_main")
    html_version =  main_post.get_attribute('outerHTML')
    soup = BeautifulSoup(html_version, 'html.parser')  
    rich_text = Extract_Text_With_Tags(soup)


    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_name = 'TextFiles'
    file_path = os.path.join(current_dir,folder_name ,'Raw_Data_'+ str(year) +'.txt')
    # Dumps the text into a file 

    with open(file_path, 'w', encoding= 'utf-8') as file:
        file.write(rich_text)
    #exits the driver
    driver.close()
    # Close the file
    file.close()
    #loads the driver and waits for it to load

