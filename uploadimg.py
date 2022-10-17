import base64, requests
from tempfile import NamedTemporaryFile

def header(user, password):
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header_json = {'Authorization': 'Basic ' + token.decode('utf-8'),
                   'Content-Disposition' : 'attachment; filename=%s'% "test1.jpg"}
    return header_json

def upload_image_to_wordpress(file_path, header_json):
    media = {'file': file_path,'caption': 'My great demo picture', 'id': 600}
    responce = requests.post("http://localhost/wordpress/wordpress//wp-json/wp/v2/media", headers = header_json, files = media)
    print(responce.text)



heder = header("admin","AX5Z kH3C o9M3 v0Xd NvC8 5hXC") #username, application password
url  = 'https://mekongnama.com.vn/wp-content/uploads/2021/07/vuong-quoc-anh-1.jpg'
raw = requests.get(url).content
with NamedTemporaryFile(delete=False,mode="wb",suffix=".jpg") as img :
    img.write(raw)
    # print(f.file())
    c  =  open(img.name,"rb")
    print(c)
    print("i,g ",img.name)
    #upload_image_to_wordpress(c,heder)