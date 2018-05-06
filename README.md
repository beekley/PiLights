# PiLights

A Raspberry Pi-based web GUI controller for WS281x programmable LED strips.

## Getting Started

These instructions will get you a copy of the project up and running on your Raspberry Pi (RPI).

### Prerequisites

This project requires the following hardware:

1. RPI with Raspbian
2. Neopixel-supported LED array (I used https://www.amazon.com/gp/product/B00B4UKG2W/)

Follow this guide for how to wire the RPI and LEDs and how to install the prerequisite neopixel software: https://learn.adafruit.com/neopixels-on-raspberry-pi/software

You can check if prereqs have been correctly completed by running the following inside the `rpi_ws281x/python/examples` directory. More configuration information here: https://learn.adafruit.com/neopixels-on-raspberry-pi/software#strandtest-example

```
sudo python strandtest.py
```

### Installation

To set up PiLights on your RPI, first  clone down the project. You may want to change directory if your terminal window is still in some `rpi_ws281x/` subdirectory (e.g. by running `cd /home/pi`).

```
git clone https://github.com/beekley/PiLights.git
```

Next, update the `hardware.py` file with your hardware configuration, according to the neopixel config link from the prerequisite section.

```
cd PiLights
nano hardware.py
```

Finally, start the server.

```
sudo python3 server_new.py
```

The web GUI should be available at:

```
raspberrypi.local:4000/client/client_new.html
```

Note: on non-apple/linux devices, you may need to use the IP address of the RPI instead of the hostname (e.g. `1.2.3.4:4000/...`).

### Running the service automatically on boot

The PiLights service can be run as a daemon that starts with on boot of the RPI and restarts on crash. To set this up, copy the `pilights.service` file to `systemd` and enable the service.

```
sudo cp pilights.service /etc/systemd/system/pilights.service
sudo systemctl enable pilights.service
```

More information is available on the RPI documentation: https://www.raspberrypi.org/documentation/linux/usage/systemd.md

## Next Steps

- [ ] Clean up references to `*_new` files and remove old files
- [ ] Pass parameters from frontend to backend (e.g. set LED color from GUI)
- [ ] Turn lights off from frontend
- [ ] Clear the queue from the frontend
- [ ] Dockerize the app
- [ ] Load list of patterns and their descriptions from backend to frontend

## Footer

PRs/issues/suggestions are encouraged and appreciated! This project was completed as part of the Day9 30 day challenge.
