import os
import threading

import requests
import yaml


# Client class to obtain image via HTTP request
class Client:
    def __init__(self, serverUri, serverPort) -> None:
        self.serverUri = serverUri
        self.serverPort = serverPort
        self.has_end = False
        self.image_path = ""
        self.success_flag = False

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
        self.success_flag = r.status_code == 200

        # Save image to file
        path = "img.png"
        # self.image_path = "datas/received/" + path
        self.image_path = path
        with open(self.image_path, "wb") as f:
            f.write(r.content)

        self.has_end = True

    def is_success(self):
        return self.success_flag


def setup():

    # Load config file from current working directory
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")
    config_path = cwd + "/ai-config/config.yml"
    print(f"Config path: {config_path}")
    with open(config_path) as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    return config
