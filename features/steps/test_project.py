# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestMyFirstTest(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_run_a_simple_test(self):
        # Given we have behave installed
        self.actionwords.we_have_behave_installed()
        # When we implement a test
        self.actionwords.we_implement_a_test()
        # Then trial will test it for us!
        self.actionwords.trial_will_test_it_for_us()
