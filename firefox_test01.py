# Simple assignment
from selenium.webdriver import Firefox
# import Keys class from selenium
from selenium.webdriver.common.keys import Keys
# import Select class from selenium
from selenium.webdriver.support.ui import Select
# import time module from python lib
import time


ffdriver = Firefox(
    executable_path='/Users/admin/Documents/Coding/python_files/geckodriver')

# variable assignment
name = "Alan"
email = "ashepherd71@outlook.com"
age = 49

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

time.sleep(1)
# locate email text field using css selector
emailTextBox = ffdriver.find_element_by_css_selector(".form__email-input")

# clear email text field
emailTextBox.clear()

# enter email into email text field
emailTextBox.send_keys(email)

time.sleep(1)
# Select the age input field
ageSelector = ffdriver.find_element_by_class_name("form__age-input")

ageSelector.click()
# clear the age input field
ageSelector.send_keys(age)

# select an option from the role drop-down
roleSelector = Select(ffdriver.find_element_by_id("role"))

time.sleep(1)

# select the Parent option from the drop-down
roleSelector.select_by_visible_text('Parent')

time.sleep(1)

# locate recommend section radio button section and click on 'Maybe'
ffdriver.find_element_by_css_selector(
    "#maybe").click()

time.sleep(1)

# select an option from the 'like' drop-down
likeSelector = Select(ffdriver.find_element_by_id("like-options"))

# select the 'Articles' option from the drop-down
likeSelector.select_by_visible_text('Articles')

time.sleep(1)

# create list of options in the improvement section
improveSelections = ["back-end", "front-end", "data-visualization"]

# select two options from the improvement section
improveSelector = ffdriver.find_element_by_css_selector(
    ".form__improvements-options")



# loop through the child elements and click/select the ones that match those give
# for i in improveSelections:
#     if


######### VERIFICATION #########
# pause until page loads
time.sleep(2)
# switch to last opened window
# ffdriver.switch_to.window(ffdriver.window_handles[-1])


# wait 10 seconds
time.sleep(5)

print(base_url)
# close the browser/webdriver
ffdriver.close()
