from selenium import webdriver

my_driver = webdriver.Chrome(executable_path="C:/chromedriver")

my_driver.get("https://www.facebook.com/")
my_driver.find_element_by_id("email").send_keys("dors@gmail.com")
my_driver.find_element_by_id("pass").send_keys("12345678")

my_driver.close()
