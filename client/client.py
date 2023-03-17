import requests


class ClientSketchTattooClassifier():

    def __init__(
        self,
        host: str = 'http://localhost',
        port: str = '8000'
    ):
        self.url = host + ':' + port

    def img2type(self, image):
        files = {'image': image}
        response = requests.post(self.url+'/file', files=files)
        content = response.json()
        return content

    def img_path2type(self, img_path: str):
        with open(img_path, 'rb') as file:
            image = file.read()
        content = self.img2type(image)
        return content

    def img_url2type(self, url: str):
        params = {'url': url}
        response = requests.post(self.url+'/link', params=params)
        content = response.json()
        return content
