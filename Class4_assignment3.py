from selenium import webdriver
from time import sleep

my_driver = webdriver.Chrome(executable_path="C:/chromedriver")

# Connect to Youtube
website = "https://www.youtube.com/"
my_driver.get(website)

# Insert something within the search box
x_path = "//html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/div/div[2]/input"
html_id = "search"
send_input = "infinity"
my_driver.find_element_by_xpath(x_path).send_keys(send_input)
my_driver.find_element_by_xpath("//*[@id=\"search-icon-legacy\"]/yt-icon").click()
sleep(3)
my_driver.close()
