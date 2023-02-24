from selenium import webdriver

import parametrs
from parts.services.item_add_steps import category_adding, cookie_setting, main_image_adding, item_information_adding, \
    package_choosing, confirm_item_adding, nem_and_mit_auth

URL = 'https://www.dba.dk/'
URL_1 = 'https://www.dba.dk/opret-annonce/'


def item_adding():
    browser = webdriver.Chrome()

    cookie_setting(browser, URL, URL_1)

    category_adding(browser,
                    parametrs.first_category_value,
                    parametrs.second_category_value,
                    parametrs.third_category_value)

    item_information_adding(browser, parametrs.item_data)
    main_image_adding(browser, parametrs.FIRST_PHOTO_PATH)
    package_choosing(browser, parametrs.package)
    confirm_item_adding(browser)
    nem_and_mit_auth(browser)
