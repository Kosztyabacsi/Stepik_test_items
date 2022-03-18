import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button is not None, "No button Add-to-basket!"

