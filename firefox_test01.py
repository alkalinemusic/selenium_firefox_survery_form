# Simple assignment
from selenium.webdriver import Firefox
# import Keys class from selenium
from selenium.webdriver.common.keys import Keys
# import time module from python lib
import time

ffdriver = Firefox(
    executable_path='/Users/admin/Documents/Coding/python_files/geckodriver')

# variable assignment
name = "Alan"
email = "ashepherd71@outlook.com"
Age = 49

# set the url to be accessed
base_url = "https://alanshepherd.dev/codesting_survey/"

# maximize window, wait 1 second, then enter url and access url
ffdriver.maximize_window()
ffdriver.implicitly_wait(1)
ffdriver.get(base_url)

# ensure "Survey Form" is in the title tag
assert "Survey Form" in ffdriver.title

# set var to value of the id name, shown in parens
nameTextBox = ffdriver.find_element_by_xpath(
    "/html/body/form/div/div[2]/div[2]/input")

# clear the name text field in the web page
nameTextBox.clear()

# enter the search_term into the name text field in the browser
nameTextBox.send_keys(name)

# initiate return keypress in the browser
nameTextBox.send_keys(Keys.TAB)


######### VERIFICATION #########
# pause until page loads
time.sleep(2)
# switch to last opened window
# ffdriver.switch_to.window(ffdriver.window_handles[-1])


# wait 10 seconds
time.sleep(10)

print(base_url)
# close the browser/webdriver
ffdriver.close()
