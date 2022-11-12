import argparse
import time

import requests
from client.client import Client, setup
from PIL import Image
from tabulate import tabulate

if __name__ == "__main__":

    # Setup the config
    config = setup()

    # Create the parser
    parser = argparse.ArgumentParser()
    # Add an argument
    parser.add_argument('--prompt', type=str, required=False, default="Lego toy house")

    # Parse the argument
    args = parser.parse_args()

    # Create client instance
    client = Client(config['serverUri'], config['serverPort'], config["id"])
    prompt = args.prompt
    print(f"Generating with prompt: {prompt}")
    is_success, uuid = client.generate(prompt)

    if not is_success:
        print("Failed, exiting...")
        exit(-1)

    try:
        last_run = time.time()

        while True:

            if last_run - time.time() > 30: # 30 seconds

                # Query for the status before getting the data
                r = requests.get(
                    f"http://{config['checkingServerIP']}:{config['checkingServerPort']}/check/{uuid}")
                current_state = r.json()["current_state"]

                r = requests.get(
                    f"http://{config['checkingServerIP']}:{config['checkingServerPort']}/check")
                ret = r.json()
                count  = ret["count"]

                print(f"Current state of request {uuid}: {current_state}")
                print(f"There are currently {count} in queue")
                queued = ret["queued"]
                print(tabulate(queued, headers="keys"))
                print()

                if current_state != "Completed":
                    last_run = time.time()

                else:
                    # Generate url
                    url =  f"http://{config['serverIP']}:{config['serverPort']}/result/{uuid}"
                    r = requests.get(url, stream=True)

                    # Save image to file
                    path = "img.png"
                    with open(path, "wb") as f:
                        f.write(r.content)

                    break

        myImage = Image.open('img.png')
        myImage.show()

    except KeyboardInterrupt:
        print("Forced exit, exiting...")
        exit(-1)
