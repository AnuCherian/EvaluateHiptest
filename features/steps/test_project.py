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

    def fight_or_flight(self, achievement_level, opponent_role, reaction):
        # Given the ninja has a ""
        self.actionwords.the_ninja_has_a()
        # When attacked by ""
        self.actionwords.attacked_by()
        # Then the ninja should ""
        self.actionwords.the_ninja_should()

    def test_Fight_or_Flight_fight(self):
        self.fight_or_flight(achievement_level = 'third level black-belt', opponent_role = 'samurai', reaction = 'engage the opponent')

    def test_Fight_or_Flight_flight(self):
        self.fight_or_flight(achievement_level = 'third level black-belt', opponent_role = 'Chuck Norris', reaction = 'run for his life')