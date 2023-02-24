import requests

def upload_file(photo_path):
    url = 'https://www.dba.dk/ajax/syi/PictureUpload/UploadFiles'

    files = {'media': open(photo_path, 'rb')}

    result = requests.post(url, files=files)

    return result.text.split(',')[1].split('"')[-2]

