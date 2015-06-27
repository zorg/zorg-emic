from zorg.driver import Driver
from multiprocessing import Queue
from time import sleep


class Emic2(Driver):

    def __init__(self, options, connection):
        super(Emic2, self).__init__(options, connection)

        self.timer = 200
        self.currentAction = 'idle'
        self.baudrate = 9600
        self.queue = Queue()

        self.commands += [
            "speak", "set_voice", "set_language",
            "set_volume", "set_rate", "pause", "stop"
        ]

    def start(self):
        # Setup involves writing a new line to initialize the board
        self.connection.write('\n')

        # Pause for 200 milliseconds
        sleep(0.02)

    def speak(self, text):
        """
        The main function to convert text into speech.
        """
        self.queue.put(text)

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
        #self.queue.put()
        self.currentAction = 'setting voice';
        self.connection.write('N' + voice + '\n');

    def set_language(self, language, dialect=None):
        """
        Set the language used for TTS.
        en: English
        es: Spanish | [ lan: latino or ca: castilian ] 
        """
        #self.queue.put()
        self.currentAction = 'setting language';
        l = 0;
        if lan == 'en':
            l = 0;
        elif lan == 'es':
            pass
            #l = typeof op === 'undefined' ? 1 : (op === 'lan' ? 2 : 1 )

        self.connection.write('l' + l + '\n')

    def set_volume(self, volume):
        """
        Set the volume of the Emic 2.
        Volume range [-48 to 18] 
        -48 (softest) to 18 (loudest)
        """
        #self.queue.put()
        self.currentAction = 'setting volume'
        self.connection.write('V' + vol + '\n')

    def set_rate(self, rate):
        """
        Set the speaking rate in words per minute.
        From 75 (slowest) to 600 (fastest).
        Default value: 200.
        """
        #self.queue.put()
        self.currentAction = 'setting rate'
        self.connection.write('W' + rate + '\n')

    def pause(self):
        """
        Immediately pause current message.
        """
        self.currentAction = 'paused'
        self.connection.write('Z\n')

    def stop(self):
        """
        Immediately stop the current message from being spoken.
        This command is only valid while a message is playing.
        """
        self.currentAction = 'stopped'
        self.connection.write('X\n')


    def reset(self):
        """
        Reset the current message beign spoken.
        """
        #self.queue.put()
        self.currentAction = 'resetting'
        self.connection.write('R\n')

