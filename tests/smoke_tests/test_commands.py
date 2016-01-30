from unittest import TestCase
from zorg_emic import Emic2


class SmokeTestCase(TestCase):

    def setUp(self):
        self.connection = None
        self.options = {}


class Emic2SmokeTests(SmokeTestCase):

    def test_command_method_exists(self):
        """
        Check that each command listed has a corresponding
        method on the driver class.
        """
        emic2 = Emic2(self.options, self.connection)

        for command in emic2.commands:
            self.assertIn(command, dir(emic2))

