import requests
import base64
import random
import urllib.request

# Tai anh tu url ve local folder hien tai
def download_image(url):
    name = random.randrange(10000000, 100000000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)
    return fullname

# Khoi tao header
def header(user, password):
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header_json = {'Authorization': 'Basic ' + token.decode('utf-8')}
    return header_json

# Upload image len wordpress
def upload_image_to_wordpress(image, url, header_json):
    fileName = download_image(image)
    print(fileName)
    media = {'file': open('./' + fileName, "rb"), 'caption': 'My great demo picture'}
    responce = requests.post(url + "wp-json/wp/v2/media", headers=header_json, files=media)
    newDict = responce.json()
    print(newDict['guid']['raw'])

# goi ham thuc thi
hed = header("username", "Application Password")
upload_image_to_wordpress('http://image/url.jpg',
                          'https://wordpress-domain.com/', hed)