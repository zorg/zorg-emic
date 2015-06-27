import zorg
import time

def work (my):
    my.speech.start()

    while True:

        # Wait 1 second before doing it again
        time.sleep(1)

robot = zorg.robot({
    "connections": {
        "firmata": {
            "adaptor": "zorg_firmata.Firmata",
            "port": "/dev/ttyUSB0",
        },
    },
    "devices": {
        "speech": {
            "connection": "firmata",
            "driver": "zorg_emic.Emic2",
        }
    },
    "name": "example", # Give your robot a unique name
    "work": work, # The method (on the main level) where the work will be done
})

robot.start()
