from PIL import Image

from client.client import Client, setup

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
