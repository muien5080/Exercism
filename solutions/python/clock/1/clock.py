class Clock:
    def __init__(self, hour, minute):
        # Normalize the time to fit in 24-hour format
        total_minutes = (hour * 60 + minute) % (24 * 60)
        self.hour = total_minutes // 60
        self.minute = total_minutes % 60

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return False
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        total_minutes = (self.hour * 60 + self.minute + minutes) % (24 * 60)
        return Clock(total_minutes // 60, total_minutes % 60)

    def __sub__(self, minutes):
        total_minutes = (self.hour * 60 + self.minute - minutes) % (24 * 60)
        return Clock(total_minutes // 60, total_minutes % 60)