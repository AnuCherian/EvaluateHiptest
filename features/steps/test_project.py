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

    def test_weaker_opponent(self):
        # Given the ninja has a third level black-belt
        self.actionwords.the_ninja_has_a_third_level_blackbelt()
        # When attacked by a samurai
        self.actionwords.attacked_by_a_samurai()
        # Then the ninja should engage the opponent
        self.actionwords.the_ninja_should_engage_the_opponent()

    def test_stronger_opponent(self):
        # Given the ninja has a third level black-belt
        self.actionwords.the_ninja_has_a_third_level_blackbelt()
        # When attacked by Chuck Norris
        self.actionwords.attacked_by_chuck_norris()
        # Then the ninja should run for his life
        self.actionwords.the_ninja_should_run_for_his_life()