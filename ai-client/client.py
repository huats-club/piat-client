import os
import threading

import requests
import yaml
from PIL import Image, ImageOps


# Client class to obtain image via HTTP request
class Client:
    def __init__(self, serverUri, serverPort) -> None:
        self.serverUri = serverUri
        self.serverPort = serverPort
        self.has_end = False
        self.image_path = ""

    def generate(self, sentence):
        self.thread = threading.Thread(target = self._generate, args=(sentence,))
        self.thread.start()

    def is_ready(self):
        if self.has_end == True:
            self.thread.join()
            self.has_end = False
            return True
        else:
            return False

    def get_image_path(self):
        return self.image_path

    # Internal method call to ensure asynchronous running
    def _generate(self, sentence):

        self.has_end = False

        # Generate query string
        tokens = sentence.split(' ')
        query = ""
        for count in range(1, len(tokens)+1):
            idx = count - 1
            query += f"token{count}={tokens[idx]}"

            if count != len(tokens):
                query += "&"

        # Generate url
        url =  f"http://{self.serverUri}:{self.serverPort}/gen?{query}"

        r = requests.get(url, stream=True)

        # Save image to file
        path = "img.png"
        # self.image_path = "datas/received/" + path
        self.image_path = path
        with open(self.image_path, "wb") as f:
            f.write(r.content)

        self.has_end = True


def setup():

    # Load config file from current working directory
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")
    config_path = cwd + "/ai-config/config.yml"
    print(f"Config path: {config_path}")
    with open(config_path) as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    # Create folder to save received image
    output_dir = os.getcwd() + "/datas/received"
    print(f"Output dir path: {output_dir}")
    if not os.path.exists("datas/received"):
        os.mkdir("datas")
        os.mkdir("datas/received")

    return config



if __name__ == "__main__":

    # Setup the config
    config = setup()

    # Create client instance
    client = Client(config['serverUri'], config['serverPort'])
    prompt = "Lego toy house"
    print(f"Generating with prompt: {prompt}")
    client.generate(prompt)

    while not client.is_ready():
        pass

    # Display image in memory
    myImage = Image.open('img.png')
    myImage.show()
