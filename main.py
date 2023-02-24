import time

import parametrs
from parts.item_add import item_adding
from parts.login import login


# Авторизация
login(parametrs.LOGIN, parametrs.PASSWORD)

# Добавление товара
item_adding()