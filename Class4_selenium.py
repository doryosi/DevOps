from selenium import webdriver
from time import sleep

my_driver = webdriver.Chrome(executable_path="C:/chromedriver")
my_driver.get("C:/Users/dorsi/Downloads/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[4]").click()
my_driver.find_element_by_id("calculate").click()
expected = "3.00"
actual = my_driver.find_element_by_id("tip").text
if expected == actual:
    print("all good")
else:
    print("top is not good")
