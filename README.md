# piat-client
Tested on
Hardware: **Raspberry Pi 4 Model B** <br>
Operating System: **Buster Full** / **Bullseye Full 64 bits**


## Dependencies
Install yaml package into raspberry pi
```
sudo apt install python3-yaml
```
Install tabulate
```
sudo pip3 install tabulate
```

## Setting Up
Please ensure respective **client raspberry pi** has the following directory
```
~/piat-client/
|   client.py

/boot/
|   ckt.hm (create for each unique client, e.g. Group_A)
```

## Sending Prompt
1. Change directory to **piat-client**
```
cd ~/piat-client
```

2. Run client.py
```
python3 -B run.py --prompt "Seed String Text"
```