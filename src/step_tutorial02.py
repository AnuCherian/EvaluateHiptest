
class NinjaFight(object):
    """
    Domain model for ninja fights.
    """
    # pylint: disable=R0903

    def __init__(self, with_ninja_level=None):
        self.with_ninja_level = with_ninja_level
        self.opponent = None

    def decision(self):
        """
        Business logic how a Ninja should react to increase his survival rate.
        """
        assert self.sut.with_ninja_level is not None
        assert self.sut.opponent is not None
        if self.sut.opponent == "Chuck Norris":
            return "run for his life"
        if "black-belt" in self.sut.with_ninja_level:
            return "engage the opponent"
        else:
            return "run for his life"