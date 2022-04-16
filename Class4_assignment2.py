from selenium import webdriver
from time import sleep

my_driver = webdriver.Chrome(executable_path="C:/chromedriver")

# Connect to Google translate
website = "http://translate.google.co.il/?hl=iw"
my_driver.get(website)

# Insert something in the hebrew box
x_path = "//*[@id=\"yDmH0d\"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea"
send_input = "שלום"
my_driver.find_element_by_xpath(x_path).send_keys(send_input)

# Wait for 5 seconds and close the browser
sleep(5)
my_driver.close()
