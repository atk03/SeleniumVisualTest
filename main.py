from functions import get_cell, wait_for_ajax, readonly_check, wait_until
from pages import Model, Company, HWCategory, Quantity
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
    model = Model(driver)
    company = Company(driver)
    hw_category = HWCategory(driver)
    quantity = Quantity(driver)
    print('--------- TEST 0: input permission ---------')

    if readonly_check(model.input_form):
        passed += 1
    else:
        failed += 1
        print('fail on: model')

    if readonly_check(company.input_form):
        passed += 1
    else:
        failed += 1
        print('fail on: company')

    if readonly_check(hw_category.input_form):
        passed += 1
    else:
        failed += 1
        print('fail on: hw_category')

    if readonly_check(quantity.input_form):
        failed += 1
        print('fail on: quantity')
    else:
        passed += 1

    print('--------- TEST 1: open - close table modal ---------')

    model.modal_btn.click()
    wait_for_ajax(driver)
    if model.table == driver.find_element_by_id('model-name'):
        passed += 1
    else:
        failed += 1
        print('fail on: model')

    model.x_btn.click()
    wait_until(driver, By.XPATH, "//body[@class='']")
    if driver.find_element_by_tag_name('body').get_attribute('class') == '':
        passed += 1
    else:
        failed += 1
        print('fail on: model')
    driver.refresh()

    print('--------- TEST 2: datatable features ---------')

    model.modal_btn.click()
    wait_for_ajax(driver)
    model.select_length.click()
    wait_for_ajax(driver)
    string_test = 'a'
    model.general_search = string_test
    model.general_search.clear()
    wait_for_ajax(driver)
    model.column_search = 'e'
    wait_for_ajax(driver)
    model.sort_btn.click()
    wait_for_ajax(driver)
    single_cell = get_cell(model.table, 3, 0)
    value = single_cell.text
    single_cell.click()
    wait_for_ajax(driver)
    model.confirm_btn.click()
    wait_for_ajax(driver)
    if model.input_form.get_attribute("value") == value and model.input_type.get_attribute("value") != '' and model.input_manufacturer.get_attribute("value") != '':
        passed += 1
    else:
        print('Input is wrong')

    print('--------- TEST 3: modal btn ---------')

    model.modal_btn.click()
    wait_for_ajax(driver)
    model.cancel_btn.click()
    wait_until(driver, By.XPATH, "//body[@class='']")
    if driver.find_element_by_tag_name('body').get_attribute('class') == '':
        passed += 1
    else:
        failed += 1
        print('fail on: model')
