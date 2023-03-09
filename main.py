import yeelight


_BULB_NAME = "sams-yeelight"


def main():
    # get all bulbs on the network
    bulbs = yeelight.discover_bulbs()

    # find the bulb you want to control
    bulb = next(bulb for bulb in bulbs if bulb["capabilities"]["name"] == _BULB_NAME)

    # create a Yeelight object
    yeelight_bulb = yeelight.Bulb(bulb["ip"])

    # turn on the bulb
    yeelight_bulb.turn_on()


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    main()
