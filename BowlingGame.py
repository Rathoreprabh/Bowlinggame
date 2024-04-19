class BowlingGame:
    def __init__(self):
       
        self.rolls = []

    def roll(self, pins):
        
        self.rolls.append(pins)

    def score(self):
        
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
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
       
        return sum(self.rolls[roll_index:roll_index+2]) == 10

    def strike_score(self, roll_index):
        
        return 10 + sum(self.rolls[roll_index + 1:roll_index + 3])

    def spare_score(self, roll_index):
       
        return 10 + self.rolls[roll_index + 2]

    def frame_score(self, roll_index):
       
        return sum(self.rolls[roll_index:roll_index+2])
