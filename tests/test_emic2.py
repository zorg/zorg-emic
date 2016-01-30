# -*- coding: utf-8 -*-

from unittest import TestCase
from zorg_emic import Emic2


class TestEmic2(TestCase):

    def setUp(self):
        self.emic = Emic2({}, None)

    def test_valid_text(self):
        self.assertTrue(
            self.emic.is_valid_string("!AaZz~")
        )

    def test_invalid_text(self):
        self.assertFalse(
            self.emic.is_valid_string("∞")
        )
