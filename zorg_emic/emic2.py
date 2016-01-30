from zorg.driver import Driver
from multiprocessing import Queue
from threading import Thread
import time


class Emic2(Driver):

    def __init__(self, options, connection):
        super(Emic2, self).__init__(options, connection)

        self.currentAction = 'idle'
        self.queue = Queue()
        self.thread = Thread(target=self.watch, args=())
        self.thread.daemon = True

        self.commands += [
            "speak", "set_voice", "set_language",
            "set_volume", "set_rate", "set_parser",
            "pause", "stop"
        ]

    def watch(self):
        while True:
            waiting = True

            # Wait if the queue is empty
            if self.queue.empty():
                time.sleep(0.5)
                continue

            while waiting:
                self.connection.serial.write("\n")
                time.sleep(0.3)
                data = self.connection.serial_read()

                # The Emic 2 transmits a ":" when ready to receive commands
                if data == ':':
                    value = self.queue.get()
                    self.connection.serial_write("%s\n" % (value))
                    waiting = False
                time.sleep(0.5)

        self.connection.disconnect()

    def start(self):
        self.connection.connect()

        # Setup involves writing a new line to initialize the board
        self.connection.serial_write('\n')

        # Pause for 500 milliseconds
        time.sleep(0.05)

        # Start a background thread to process items in the queue
        self.thread.start()

    def is_valid_string(self, text):
        """
        The Emic 2 expects characters that conform to the ISO-8859-1 Latin
        character set. This method will return false if a string is not
        ISO-8859-1 compatible.
        """
        return all(ord(character) < 128 for character in text)

    def speak(self, text):
        """
        The main function to convert text into speech.
        """
        if not self.is_valid_string(text):
            raise Exception("%s is not ISO-8859-1 compatible." % (text))

        self.queue.put("S%s" % (text))

    def set_voice(self, voice):
        """
        Change between 9 available voices on the Emic2.
        0: Perfect Paul (Paulo)
        1: Huge Harry (Francisco)
        2: Beautiful Betty
        3: Uppity Ursula
        4: Doctor Dennis (Enrique)
        5: Kit the Kid
        6: Frail Frank
        7: Rough Rita
        8: Whispering Wendy (Beatriz)
        """
        self.currentAction = 'setting voice';
        self.queue.put('N%d' % (voice));

    def set_language(self, language, dialect=None):
        """
        Set the language used for TTS.
        en: English
        es: Spanish | [ lan: latino or ca: castilian ] 
        """
        self.currentAction = 'setting language';
        l = 0;
        if language == 'en':
            l = 0;
        elif language == 'es':
            l = 1

            if dialect == 'ca':
                l = 2

        self.queue.put('l%s' % (l))

    def set_volume(self, volume):
        """
        Set the volume of the Emic 2.
        Volume range [-48 to 18] 
        -48 (softest) to 18 (loudest)
        """
        self.currentAction = 'setting volume'
        self.queue.put('V%d' % (volume))

    def set_rate(self, rate):
        """
        Set the speaking rate in words per minute.
        From 75 (slowest) to 600 (fastest).
        Default value: 200.
        """
        self.currentAction = 'setting rate'
        self.queue.put('W%d' % (rate))

    def set_parser(parser):
        """
        Select either the Epson or DECtalk text parsing engine.
        0 DECtalk
        1 Epson (default)
        """
        self.queue.put('P%d' % (parser))

    def pause(self):
        """
        Immediately pause current message.
        """
        self.currentAction = 'paused'
        self.queue.put('Z')

    def stop(self):
        """
        Immediately stop the current message from being spoken.
        This command is only valid while a message is playing.
        """
        self.currentAction = 'stopped'
        self.queue.put('X')

    def reset(self):
        """
        Reset the current message beign spoken.
        """
        self.currentAction = 'resetting'
        self.queue.put('R')
