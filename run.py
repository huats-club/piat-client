import argparse
import time

from PIL import Image

from client.client import Client, setup

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
    client = Client(config['serverUri'], config['serverPort'])
    prompt = args.prompt
    print(f"Generating with prompt: {prompt}")
    client.generate(prompt)

    last = time.now()
    print("Running", end="")
    while not client.is_ready():
        if time.now() - last > 30:
            print(".", end="")
        pass
    print("Done")

    if client.is_success():
        # Display image in memory
        myImage = Image.open('img.png')
        myImage.show()

    else:
        print("Failed")