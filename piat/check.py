import requests
from client.client import setup
from tabulate import tabulate

if __name__ == "__main__":

    # Setup the config
    config = setup()

    r = requests.get(
        f"http://{config['checkingServerIP']}:{config['checkingServerPort']}/check")

    json_ret = r.json()

    count = json_ret["count"]
    if count == 0:
        print("Queue is currently empty!")
        print()

    else:
        print(f"There are currently {count} in queue")
        queued = json_ret["queued"]
        print(tabulate(queued, headers="keys"))
