class Game(object):
    """
    Represents a single player's bowling game, and calculates their score.
    """

    # Represent the game as a series of balls, rather than as a series of
    # frames. We should be able to break this up into frames fine, and it
    # means, for example, when we come to score a strike we don't need to
    # worry if the next two balls span two frames (i.e. the first is a
    # strike also). We won't record imaginary balls after strikes just for the
    # sake of being able to split into frames every second ball, so splitting
    # will need to account for strikes.

    def __init__(self, balls=''):
        self.balls = balls
