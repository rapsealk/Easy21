#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from easy21 import Easy21   # noqa: E402


class Easy21TestCase(unittest.TestCase):

    def setUp(self):
        self.env = Easy21()
        self.state = self.env.reset()

    def test_go_bust(self):
        for i in range(21):
            self.assertFalse(self.env.goes_bust(i+1))
        self.assertTrue(self.env.goes_bust(0))
        self.assertTrue(self.env.goes_bust(22))

    """
    def test_play_out(self):
        player = 18
        dealer = 18
        self.assertEqual(self.env.__play_out(player, dealer), 0)
    """


if __name__ == "__main__":
    unittest.main()
