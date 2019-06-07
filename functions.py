from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#
#credits to Prashanth Sams
# https://stackoverflow.com/questions/24053671/webdriver-wait-for-ajax-request-in-python)
# Waits until ajax's call ends;
# @params: webdriver driver
#
def wait_for_ajax(driver):
    wait = WebDriverWait(driver, 15)
    try:
        wait.until(lambda driver: driver.execute_script('return jQuery.active') == 0)
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    except Exception as e:
        pass


#
# Returns table's cell
# @param: webelement table
# @param: int i row's index
# @param: int j column's index
# @return: webelement cell
#
def get_cell(table, i, j):
    row = table.find_elements_by_css_selector('tr')
    try:
        cell = row[i].find_elements_by_tag_name('td')
        return cell[j]
    except IndexError:
        pass

#
# Check input permission
# @param: webelement input_id
# @return: bool True if input is read-only
#
def readonly_check(input_id):
    if input_id.get_attribute('data-readonly') == '':
        return True
    else:
        return False


#
# Waits until element is in page;
# https://selenium-python.readthedocs.io/waits.html
# @params: webdriver driver
# @param: By selector strategies to locate elements
# @param: string el element to search
#
def wait_until(driver, selector, el):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((selector, el)))
