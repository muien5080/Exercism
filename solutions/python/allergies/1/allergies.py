class Allergies:
    ALLERGENS = [
        ("eggs", 1),
        ("peanuts", 2),
        ("shellfish", 4),
        ("strawberries", 8),
        ("tomatoes", 16),
        ("chocolate", 32),
        ("pollen", 64),
        ("cats", 128),
    ]

    def __init__(self, score):
        # Keep only relevant bits (0–255)
        self.score = score % 256

    def allergic_to(self, item):
        for allergen, value in self.ALLERGENS:
            if allergen == item:
                return bool(self.score & value)
        return False

    @property
    def lst(self):
        return [
            allergen
            for allergen, value in self.ALLERGENS
            if self.score & value
        ]