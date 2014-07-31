class InvalidFrame(Exception):
    pass


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

    def _ball_to_value(self, ball, previous=None):
        # turn a string representing a ball's score into an integer
        try:
            ball_score = int(ball)
        except ValueError as e:
            if ball.lower() == 'x':
                return 10
            if ball == '/':
                return 10 - previous
            message = ("{} is not a valid score for a ball".format(ball))
            raise type(e)(message)
        else:
            return ball_score

    def _make_balls_array(self):
        # turn the string into an array of integers
        balls_array = []
        previous = None
        for x in self.balls:
            ball_score = self._ball_to_value(x, previous)
            previous = ball_score
            balls_array.append(ball_score)
        return balls_array

    def calculate_score(self):
        return self._score_loop(score=0, frame=1, balls=self._make_balls_array())

    def _score_loop(self, score=0, frame=0, balls=[]):
        if balls[0] == 10:
            # strike!
            score+=sum(balls[:3]) # score this ball and the next two
            balls=balls[1:] # get rid of this ball
        else:
            two_ball_sum = sum(balls[:2])
            if two_ball_sum < 10:
                score+=two_ball_sum # score the two balls
            elif two_ball_sum == 10:
                # spare
                score+=sum(balls[:3]) # score these two balls and the next one
            else:
                # somebody's cheating...
                raise InvalidFrame(
                    "Balls in frame {} add up to more than 10".format(frame)
                )
            balls=balls[2:] # get rid of both balls

        if frame == 10 or not balls:
            # we don't actually ever insist that a frame be two balls, we just
            # treat them that way (except in strikes) and score subsequent balls
            # for bonuses. So, when it comes to frame 10 being extendable to a
            # third ball, our scoring method doesn't actually have to account
            # for this in a special way. We'll care to look at what's left if
            # we do validation, but here it's just not needed.
            return (score, frame)
        return self._score_loop(score=score, frame=frame+1, balls=balls)
