from functions import get_cell, wait_for_ajax, readonly_check, wait_until
from pages import MyClass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# create capabilities
capabilities = DesiredCapabilities.INTERNETEXPLORER
# delete platform and version keys
capabilities.pop("platform", None)
capabilities.pop("version", None)

# create a new browser session
driver1 = webdriver.Chrome()
driver2 = webdriver.Firefox()
driver3 = webdriver.Ie(capabilities=capabilities)
drivers = [driver1, driver2, driver3]

for driver in drivers:
    url = "http://localhost"
    driver.get(url)
    null = 0
    failed = 0
    passed = 0

    #page to test
    my_id = MyClass(driver)
    print('--------- TEST 0: input permission ---------')

    if readonly_check(my_id.input_form):
        passed += 1
    else:
        failed += 1
        print('fail on: my_id')

   

    print('--------- TEST 1: open - close table modal ---------')

    my_id.modal_btn.click()
    wait_for_ajax(driver)
    if my_id.table == driver.find_element_by_id('my_id'):
        passed += 1
    else:
        failed += 1
        print('fail on: my_id')

    my_id.x_btn.click()
    wait_until(driver, By.XPATH, "//body[@class='']")
    if driver.find_element_by_tag_name('body').get_attribute('class') == '':
        passed += 1
    else:
        failed += 1
        print('fail on: my_id')
    driver.refresh()

    print('--------- TEST 2:  features ---------')

    my_id.modal_btn.click()
    wait_for_ajax(driver)
    single_cell = get_cell(my_id.table, 3, 0)
    value = single_cell.text


    print('--------- TEST 3: modal btn ---------')

    model.modal_btn.click()
    wait_for_ajax(driver)
    model.cancel_btn.click()
    wait_until(driver, By.XPATH, "//body[@class='']")
    if my_id.find_element_by_tag_name('body').get_attribute('class') == '':
        passed += 1
    else:
        failed += 1
        print('fail on: my_id')
