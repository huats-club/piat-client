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

    try:

        last_run = time.time()

        while True:


            if time.time() - last_run > 15 * 60: # Every 15 mins

                print("TIMEOUT: RUNNING SD")

                # Create client instance
                client = Client(config['serverUri'], config['serverPort'], config["id"])
                prompt = args.prompt
                print(f"Generating with prompt: {prompt}")
                client.generate(prompt)

                last = time.time()
                print("Running", flush= True, end="")
                while not client.is_ready():
                    difference = (time.time() - last)
                    if difference > 1:
                        print(".", flush= True, end="")
                        last = time.time()
                print("")

                if client.is_success():
                    # Display image in memory
                    myImage = Image.open('img.png')
                    myImage.show()

                else:
                    print("Failed")

                last_run = time.time()

    except KeyboardInterrupt:
        print("Exiting...")
