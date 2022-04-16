from selenium import webdriver

my_driver = webdriver.Chrome(executable_path="C:/chromedriver")
website = "http://www.walla.co.il"
expected = "וואלה"
# Connect the website
my_driver.get(website)
# Store the HTML title value within a variable
get_title = my_driver.title
# Slice the String to get the exact name of the website
actual = get_title[:5]

try:
    assert expected == actual
    print("all good")
except AssertionError:
    print("test failed")

my_driver.close()
