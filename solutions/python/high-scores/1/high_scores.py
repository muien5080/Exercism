class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        # Return the last score added
        return self.scores[-1] if self.scores else None

    def personal_best(self):
        # Return the highest score
        return max(self.scores) if self.scores else None

    def personal_top_three(self):
        # Return the top three scores in descending order
        return sorted(self.scores, reverse=True)[:3]