from selenium import webdriver

my_driver = webdriver.Chrome(executable_path="C:/chromedriver")

my_driver.get("https://translate.google.co.il/?hl=iw/")

by_id = my_driver.find_element_by_id("yDmH0d")
by_class = my_driver.find_element_by_class_name("QFw9Te")
by_xpath = my_driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
print(by_id)
print(by_class)
print(by_xpath)
my_driver.close()
