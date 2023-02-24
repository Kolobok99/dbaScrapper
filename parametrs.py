from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

LOGIN = 'izolotavin99@gmail.com'
PASSWORD = 'iyceQM6yNJe2CJu'

first_category_value = 'Mobil og telefoni'
second_category_value = 'Mobiltelefoner og tilbehør'
third_category_value = 'iPhone'

FIRST_PHOTO_PATH = f'{BASE_DIR}/photo/photo1.jpg'
SECOND_PHOTO_PATH = f'{BASE_DIR}/photo/photo2.jpg'
THIRD_PHOTO_PATH = f'{BASE_DIR}/photo/photo3.jpg'

item_data = {
    'title': 'Iphone 14 pro',
    'model': '14 Pro',
    'memory': '128',
    'color': 'guld',
    'state': 'God',
    'description': 'Very nice iphone',
    'IMEI': '352906114078126',
    'price': '1000',
}

user_territorial_data = {
    'address': 'Strand House Nybrogade 18',
    'post_number': '1212',
}

package = None