import unittest

from WiFiman import WiFiman

wfm = WiFiman()


class test(unittest.TestCase):
    def test_launch(self):
        assert wfm

    def test_Wifiman_check(self):
        assert wfm.getSpeed()
        ## This loop should go until the process is terminated to continuously gauge network speed
