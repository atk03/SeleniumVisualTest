from page_objects import PageObject, PageElement

#
# Thanks to eeaston GitHub user for this tutorial: https://github.com/eeaston/page-objects/blob/master/docs/tutorial.rst
#


class MyClass(PageObject):
    table = PageElement(id_="my_id")
    modal_btn = PageElement(xpath="//*[@data-target='#list-my_id-modal']")
    input_form = PageElement(id_='my_id')
    confirm_btn = PageElement(xpath="//button[@class='btn btn-primary btn-modal-confirm']")
    cancel_btn = PageElement(xpath="//button[@class='btn btn-secondary btn-modal-cancel']")
    previous_btn = PageElement(id_="model-name_previous")
    next_btn = PageElement(id_="model-name_next")
    x_btn = PageElement(xpath="//button[@class='close']")
