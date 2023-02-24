import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import consts

URL_2 = 'https://www.dba.dk/opret-annonce/'


def login(login, password):
    browser = webdriver.Chrome()
    browser.get(url=URL_2)

    # Ввод email
    email_input = WebDriverWait(browser, 10) \
        .until(EC.presence_of_element_located((By.ID, consts.ID_INPUT_EMAIL)))

    email_input.send_keys(login)

    confirm_email_btn = WebDriverWait(browser, 10) \
        .until(EC.presence_of_element_located((By.ID, consts.ID_CONFIRM_EMAIL_BTN)))

    confirm_email_btn.click()

    # Ввод пароля
    password_input = WebDriverWait(browser, 10) \
        .until(EC.presence_of_element_located((By.ID, consts.ID_INPUT_PASSWORD)))

    password_input.send_keys(password)

    confirm_login = WebDriverWait(browser, 10) \
        .until(EC.presence_of_element_located((By.ID, consts.ID_CONFIRM_EMAIL_AND_PASSWORD_BTN)))

    confirm_login.click()

    # Ввода кода
    WebDriverWait(browser, 10) \
        .until(EC.presence_of_element_located((By.CSS_SELECTOR, consts.SELECTOR_LOGIN_CODES_INPUTS)))

    login_codes_inputs = browser.find_elements(By.CSS_SELECTOR, consts.SELECTOR_LOGIN_CODES_INPUTS)

    codes = input()

    for i in range(len((login_codes_inputs))):
        login_codes_inputs[i].send_keys(codes[i])

    confirm_codes = WebDriverWait(browser, 10) \
        .until(EC.presence_of_element_located((By.ID, consts.ID_CONFIRM_EMAIL_AND_PASSWORD_BTN)))

    confirm_codes.click()

    WebDriverWait(browser, 20)\
        .until(EC.element_to_be_clickable((By.XPATH, consts.XPATH_SHOW_CATEGORIES_BTN)))
    # Сохранение куков
    pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))
    browser.quit()