class Scale:
    SHARPS = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
    FLATS  = ["A","Bb","B","C","Db","D","Eb","E","F","Gb","G","Ab"]

    USE_SHARPS = {
        "C","G","D","A","E","B","F#",
        "a","e","b","f#","c#","g#","d#"
    }

    def __init__(self, tonic):
        # Normalize tonic (capitalize first letter, keep accidental)
        self.tonic = tonic[0].upper() + tonic[1:]

        # Choose scale
        if tonic in self.USE_SHARPS:
            self.scale = self.SHARPS
        else:
            self.scale = self.FLATS

    def _rotated_scale(self):
        idx = self.scale.index(self.tonic)
        return self.scale[idx:] + self.scale[:idx]

    def chromatic(self):
        return self._rotated_scale()

    def interval(self, intervals):
        scale = self._rotated_scale()
        result = [scale[0]]

        i = 0
        for step in intervals:
            if step == "m":      # half step
                i += 1
            elif step == "M":    # whole step
                i += 2
            elif step == "A":    # augmented
                i += 3

            result.append(scale[i % len(scale)])

        return result