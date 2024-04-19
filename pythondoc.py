class BowlingGame:
    """
    Class to represent a game of 10-pin bowling.

    Attributes:
        rolls (list): A list to record the number of pins knocked down in each roll.
    """

    def __init__(self):
        """
        Initializes a new instance of the BowlingGame class.
        """
        self.rolls = []

    def roll(self, pins):
        """
        Record a roll in the game.
        
        Args:
            pins (int): The number of pins knocked down in this roll.
        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculate and return the total score for the game based on rolls recorded.

        Returns:
            int: The total score for the game.
        """
        total_score = 0
        roll_index = 0
        for frame in range(10):
            if self.is_strike(roll_index):
                total_score += self.strike_score(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):
                total_score += self.spare_score(roll_index)
                roll_index += 2
            else:
                total_score += self.frame_score(roll_index)
                roll_index += 2
        return total_score

    def is_strike(self, roll_index):
        """
        Determine if a given roll is a strike.

        Args:
            roll_index (int): The index of the roll to check.

        Returns:
            bool: True if the roll is a strike, otherwise False.
        """
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        """
        Determine if a given frame is a spare.

        Args:
            roll_index (int): The starting index of the frame to check.

        Returns:
            bool: True if the frame is a spare, otherwise False.
        """
        return sum(self.rolls[roll_index:roll_index+2]) == 10

    def strike_score(self, roll_index):
        """
        Calculate the score for a strike frame.

        Args:
            roll_index (int): The index of the strike roll.

        Returns:
            int: The score for this strike frame.
        """
        return 10 + sum(self.rolls[roll_index + 1:roll_index + 3])

    def spare_score(self, roll_index):
        """
        Calculate the score for a spare frame.

        Args:
            roll_index (int): The index of the first roll in the spare frame.

        Returns:
            int: The score for this spare frame.
        """
        return 10 + self.rolls[roll_index + 2]

    def frame_score(self, roll_index):
        """
        Calculate the score for a frame with no strikes or spares.

        Args:
            roll_index (int): The index of the first roll in the frame.

        Returns:
            int: The total pins knocked down in this frame.
        """
        return sum(self.rolls[roll_index:roll_index+2])
