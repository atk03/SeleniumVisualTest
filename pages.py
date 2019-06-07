from page_objects import PageObject, PageElement

#
# Thanks to eeaston GitHub user for this tutorial: https://github.com/eeaston/page-objects/blob/master/docs/tutorial.rst
#


class Model(PageObject):
    table = PageElement(id_="model-name")
    modal_btn = PageElement(xpath="//*[@data-target='#list-model-modal']")
    input_form = PageElement(id_='modelName')
    select_length = PageElement(xpath="//select[@name='model-name_length']/option[@value='25']")
    general_search = PageElement(xpath="//input[@type='search']")
    column_search = PageElement(xpath="//input[@id='txtSearch']")
    sort_btn = PageElement(xpath="//th[@tabindex='0']")
    tbl_info = PageElement(id_ ="model-name_info")
    confirm_btn = PageElement(xpath="//button[@class='btn btn-primary btn-modal-confirm']")
    cancel_btn = PageElement(xpath="//button[@class='btn btn-secondary btn-modal-cancel']")
    previous_btn = PageElement(id_="model-name_previous")
    next_btn = PageElement(id_="model-name_next")
    input_type= PageElement(id_="type")
    input_manufacturer = PageElement(id_="manufacturer")
    x_btn = PageElement(xpath="//button[@class='close']")


class Company(PageObject):
    table = PageElement(id_="company-name")
    modal_btn = PageElement(xpath="//*[@data-target='#list-company-modal']")
    input_form = PageElement(id_='company')
    select_length = PageElement(xpath="//select[@name='company-name_length']/option[@value='25']")
    general_search = PageElement(xpath="//input[@type='search']")
    column_search = PageElement(xpath="//input[@id='txtSearch']")
    sort_btn = PageElement(class_name='sorting_asc')
    tbl_info = PageElement(id_="company-name_info")
    confirm_btn = PageElement(xpath="//button[@class='btn btn-primary btn-modal-confirm']")
    cancel_btn = PageElement(xpath="//button[@class='btn btn-secondary btn-modal-cancel']")
    previous_btn = PageElement(id_="company-name_previous")
    next_btn = PageElement(id_="company-name_next")
    x_btn = PageElement(xpath="//button[@class='close']")


class HWCategory(PageObject):
    table = PageElement(id_="hw-category")
    modal_btn = PageElement(xpath="//*[@data-target='#list-hw-modal']")
    input_form = PageElement(id_='hwCategory')
    select_length = PageElement(xpath="//select[@name='hw-category_length']/option[@value='25']")
    general_search = PageElement(xpath="//input[@type='search']")
    column_search = PageElement(xpath="//input[@id='txtSearch']")
    sort_btn = PageElement(class_name='sorting_asc')
    tbl_info = PageElement(id_="hw-category_info")
    confirm_btn = PageElement(xpath="//button[@class='btn btn-primary btn-modal-confirm']")
    cancel_btn = PageElement(xpath="//button[@class='btn btn-secondary btn-modal-cancel']")
    previous_btn = PageElement(id_="hw-category_previous")
    next_btn = PageElement(id_="hw-category_next")
    x_btn = PageElement(xpath="//button[@type='button', @class='close']")


class Quantity(PageObject):
    input_form = PageElement(id_="quantity")