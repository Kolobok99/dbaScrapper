ID_INPUT_EMAIL = 'email'
ID_CONFIRM_EMAIL_BTN = 'ActionButton_0'

ID_INPUT_PASSWORD = 'password'
ID_CONFIRM_EMAIL_AND_PASSWORD_BTN = 'ActionButton_0'

SELECTOR_LOGIN_CODES_INPUTS = '#code > input'

ID_CONFIRM_CODES_BTN = 'ActionButton_0'

ID_CREATE_SELLING = 'syi-btn'

XPATH_SHOW_CATEGORIES_BTN = "//a[text()=' vælg fra liste']"

SELECTOR_SELECTS_CATEGORY = 'div.controls > select'

SELECT_ALL_FIRST_OPTIONS = 'div.controls > select:first-child > option'
SELECT_ALL_SECOND_OPTIONS = 'div.controls > select:nth-child(2) > option'
SELECT_ALL_THIRD_OPTIONS = 'div.controls > select:nth-child(3) > option'

ID_TITLE_ITEM_INPUT = 'Input_Heading'

SELECTOR_MODELS_SELECT = '#matrix-element-23497'
SELECTOR_MEMORY_SELECT = '#matrix-element-23498'
SELECTOR_COLOR_SELECT = '#matrix-element-23499'
SELECTOR_STATE_SELECT = '#matrix-element-28119'

ID_DESCRIPTION_TEXT_AREA = 'Input_AdditionalText'
ID_IMEI_NUMBER_INPUT = 'ImeiNumber'
ID_INPUT_PRICE = 'PriceId_Price'

ID_BTN_UPLOAD_IMAGE = 'uploadButton'

ID_INPUT_PRIMARY_PICTURE = 'PrimaryPicture'
def get_xpath_category_option(value):
    return f"//option[text()='{value}']"

XPATH_BTN_SPAN_WITH_OUT_PACKAGE = "//span[text()='Vælg basisannonce']"

XPATH_BTN_CONFIRM_ITEM_ADDING = "//button[text()='Næste']"

SELECTOR_HEADER_PAGE_NEM_AND_MIT_ID = '.header > .company-logo'