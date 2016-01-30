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

    def test_word_wrap(self):
        text = "aaa bb cc ddddd"
        lines = self.emic.word_wrap(text, width=6)

        self.assertEqual(len(lines), 3)

    def test_word_wrap2(self):
        text = "Robot ipsum datus scan amet, constructor ad ut splicing " \
               "elit, sed do errus mod tempor in conduit ut laboratory et " \
               "deplore electromagna aliqua. Ut enim ad minimum veniam, " \
               "quis no indestruct exoform ullamco laboris nisi ut alius " \
               "equip ex ea commando evaluant. Duis ex machina aute ire " \
               "dolorus in scan detectus an voluptate volt esse cesium " \
               "dolore eu futile nulla parameter."
        lines = self.emic.word_wrap(text, width=20)

        for line in lines:
            self.assertTrue(len(line) <= 20)
