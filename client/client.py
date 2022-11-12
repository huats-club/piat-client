import os
import threading

import requests
import yaml


# Client class to obtain image via HTTP request
class Client:
    def __init__(self, serverUri, serverPort, id=None) -> None:
        self.serverUri = serverUri
        self.serverPort = serverPort
        self.id = id

    def generate(self, sentence):
        self.thread = threading.Thread(target = self._generate, args=(sentence,))
        self.thread.start()

    # Internal method call to ensure asynchronous running
    def _generate(self, sentence):

        if self.id == None:
            self.has_end = True
            return

        self.has_end = False

        # Generate query string
        tokens = sentence.split(' ')
        query = f"token0={self.id}&"
        for count in range(1, len(tokens)+1):
            idx = count - 1
            query += f"token{count}={tokens[idx]}"

            if count != len(tokens):
                query += "&"

        # Generate url
        url =  f"http://{self.serverUri}:{self.serverPort}/gen?{query}"

        r = requests.get(url)

        if r.status_code == 200:
            return_json = r.json()
            uuid = return_json["result-id"]
            return True, uuid

        else:
            return False, ""


def setup():
    try:
        with open('/boot/ckt.hm', 'r') as file:
            data = file.read().replace('\n', '')
        config["id"] = data
    except FileNotFoundError:
        pass

    # Load config file from current working directory
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")
    config_path = cwd + "/ai-config/config.yml"
    print(f"Config path: {config_path}")
    with open(config_path) as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)


    return config
