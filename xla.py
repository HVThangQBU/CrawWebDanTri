from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc import Client
import base64, requests
from tempfile import NamedTemporaryFile
from wordpress_xmlrpc.methods import taxonomies
client = Client('http://localhost/wordpress/wordpress/xmlrpc.php',
                'admin', 'AX5Z kH3C o9M3 v0Xd NvC8 5hXC')

# # set to the path to your file
# url  = 'https://icdn.dantri.com.vn/thumb_w/680/2022/09/25/2f4cd472f4fd30a369ec-edited-1664115660838.jpeg'
# raw = requests.get(url).content
# with NamedTemporaryFile(delete=False,mode="wb",suffix=".jpg") as img :
#     img.write(raw)
#     # print(f.file())
#     c  =  open(img.name,"rb")
#     filename =img.name
#     data = {
#             'name': filename,
#             'type': 'image/jpeg',  # mimetype
#     }
#
# # read the binary file and let the XMLRPC library encode it into base64
#     with open(filename, 'rb') as img:
#         data['bits'] = xmlrpc_client.Binary(img.read())
#
#     response = client.call(media.UploadFile(data))
# # response == {
# #       'id': 6,
# #       'file': 'picture.jpg'
# #       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
# #       'type': 'image/jpeg',
# # }
# attachment_id = response['id']
post = WordPressPost()
post.title = 'Picture of the Day'
post.content = 'What a lovely picture today!'
post.post_status = 'publish'
post.terms_names = {
        'post_tag': ['tagA', 'another tag'],
        'category': ['THANG HOANG'],
}
# post.thumbnail = attachment_id
post.id = client.call(posts.NewPost(post))
# def upload_image_to_wordpress(file_path, header_json):
#     media = {'file': file_path,'caption': 'My great demo picture'}
#     responce = requests.post("http://localhost/wordpress/wordpress//wp-json/wp/v2/media", headers = header_json, files = media)
#     print(responce.text)
#
#
#
# heder = header("admin","AX5Z kH3C o9M3 v0Xd NvC8 5hXC") #username, application password
# url  = 'https://mekongnama.com.vn/wp-content/uploads/2021/07/vuong-quoc-anh-1.jpg'
# raw = requests.get(url).content
# with NamedTemporaryFile(delete=False,mode="wb",suffix=".jpg") as img :
#     img.write(raw)
#     # print(f.file())
#     c  =  open(img.name,"rb")
#     upload_image_to_wordpress(c,heder)