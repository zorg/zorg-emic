import zorg
import time

def work(my):
    my.speech.start()

    my.speech.set_voice(1)
    my.speech.speak("Upgrade in progress")

    count = 0

    while True:

        my.speech.speak(count)
        print(count)

        count = count + 1

        # Wait 1 second before doing it again
        time.sleep(1)

robot = zorg.robot({
    "connections": {
        "firmata": {
            "adaptor": "zorg_emic.Serial",
            "port": "/dev/ttyAMA0",
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
