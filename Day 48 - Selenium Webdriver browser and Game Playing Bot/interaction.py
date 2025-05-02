from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# articles.click() # click to the link

# Find element by Link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
#all_portals.click()

# Find the Search <input> by Name
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to selenium
search.send_keys("Python", Keys.ENTER)

#driver.quit() # close whole browser