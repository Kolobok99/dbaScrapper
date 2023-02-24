import pickle
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from parts import consts
from parts.services.services import upload_file


def cookie_setting(browser, init_url, url):
    browser.get(url=init_url)

    cookies_dump = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies_dump:
        browser.add_cookie(cookie)

    browser.get(url=url)

def category_adding(browser, first_category, second_category, last_category):
    # Открыть категории
    show_category_btn = WebDriverWait(browser, 10) \
        .until(EC.presence_of_element_located((By.XPATH, consts.XPATH_SHOW_CATEGORIES_BTN)))

    show_category_btn.click()

    # Выбрать категорию (Первую)
    WebDriverWait(browser, 15) \
        .until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, consts.SELECTOR_SELECTS_CATEGORY
    )))

    all_first_options = browser.find_elements(By.CSS_SELECTOR, consts.SELECT_ALL_FIRST_OPTIONS)

    for option in all_first_options:
        if option.text == first_category:
            option.click()

    # Выбрать категорию (Вторую)
    all_second_options = browser.find_elements(By.CSS_SELECTOR, consts.SELECT_ALL_SECOND_OPTIONS)

    for option in all_second_options:
        if option.text == second_category:
            option.click()

    # Выбрать категорию (Третью)
    all_third_options = browser.find_elements(By.CSS_SELECTOR, consts.SELECT_ALL_THIRD_OPTIONS)

    for option in all_third_options:
        if option.text == last_category:
            option.click()

def main_image_adding(browser, photo_path):

    btn_to_add_photo = WebDriverWait(browser, 10) \
        .until(EC.element_to_be_clickable(
        (By.ID, consts.ID_BTN_UPLOAD_IMAGE)))
    btn_to_add_photo.click()

    time.sleep(3)
    file_url = upload_file(photo_path)
    js = f"document.getElementById('{consts.ID_INPUT_PRIMARY_PICTURE}').value = '{file_url}';"
    browser.execute_script(js)

def item_information_adding(browser, item_data):

    # Заголовок
    title_input = WebDriverWait(browser, 20)\
        .until(EC.element_to_be_clickable((By.ID, consts.ID_TITLE_ITEM_INPUT)))
    title_input.send_keys(item_data['title'])

    # Модель
    models_select = Select(browser.find_element(By.CSS_SELECTOR, consts.SELECTOR_MODELS_SELECT))
    models_select.select_by_visible_text(item_data['model'])

    # Меmory
    memory_select = Select(browser.find_element(By.CSS_SELECTOR, consts.SELECTOR_MEMORY_SELECT))
    memory_select.select_by_visible_text(item_data['memory'])

    # Color
    memory_select = Select(browser.find_element(By.CSS_SELECTOR, consts.SELECTOR_COLOR_SELECT))
    memory_select.select_by_visible_text(item_data['color'])

    # State
    state_select = Select(browser.find_element(By.CSS_SELECTOR, consts.SELECTOR_STATE_SELECT))
    state_select.select_by_visible_text(item_data['state'])

    # description
    description_input = browser.find_element(By.ID, consts.ID_DESCRIPTION_TEXT_AREA)
    description_input.send_keys(item_data['description'])

    # IMEI
    imei_input = browser.find_element(By.ID, consts.ID_IMEI_NUMBER_INPUT)
    imei_input.send_keys(item_data['IMEI'])

    # PRICE
    price_input = browser.find_element(By.ID, consts.ID_INPUT_PRICE)
    price_input.send_keys(item_data['price'])


def package_choosing(browser, package):
    if not package:
        btn_with_out_package = WebDriverWait(browser, 10)\
            .until(EC.element_to_be_clickable((By.XPATH, consts.XPATH_BTN_SPAN_WITH_OUT_PACKAGE)))
        btn_with_out_package.click()

def confirm_item_adding(browser):

    confirm_btn = WebDriverWait(browser, 10) \
        .until(EC.element_to_be_clickable((By.XPATH, consts.XPATH_BTN_CONFIRM_ITEM_ADDING)))
    confirm_btn.click()

def nem_and_mit_auth(browser):
    WebDriverWait(browser, 10) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, consts.SELECTOR_HEADER_PAGE_NEM_AND_MIT_ID)))
