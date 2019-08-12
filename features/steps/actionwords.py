from src.step_tutorial02 import NinjaFight

# encoding: UTF-8
class Actionwords:
    def __init__(self, ninja_param = None):
        self.ninja_param = ninja_param
        self.sut = NinjaFight()
        pass

    def we_have_behave_installed(self):
        pass

    def we_implement_a_test(self):
        pass

    def trial_will_test_it_for_us(self):
        pass

    def the_ninja_has_a(self, achievement_level = ""):
        self.sut.with_ninja_level = achievement_level
        assert( self.sut.with_ninja_level is not None) 

    def the_ninja_should(self, reaction = ""):      
        assert(self.sut.decision() == reaction) is True
        
    def attacked_by(self, opponent_role = ""):
        self.sut.opponent = opponent_role
        assert(self.sut.opponent is not None) 
