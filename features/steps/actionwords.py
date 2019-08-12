# encoding: UTF-8
from src.step_tutorial02 import NinjaFight as NinjaFight1

class Actionwords:
    def __init__(self, ninja_param = None):
        self.ninja_param = ninja_param
        pass

    def we_have_behave_installed(self):
        pass

    def we_implement_a_test(self):
        pass

    def trial_will_test_it_for_us(self):
        pass

    def the_ninja_has_a(self, achievement_level = ""):
        NinjaFight1.with_ninja_level = achievement_level
        assert(NinjaFight1.with_ninja_level) is not None

    def the_ninja_should(self, reaction = ""):      
        assert(NinjaFight1.decision(self) == reaction) is True
        
    def attacked_by(self, opponent_role = ""):
        NinjaFight1.opponent = opponent_role
        assert(NinjaFight1.opponent) is not None
