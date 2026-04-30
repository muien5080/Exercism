class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate."""

    # Class attribute to track total aliens
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

        # Increment class counter
        Alien.total_aliens_created += 1

    def hit(self):
        """Decrement health by 1."""
        self.health -= 1

    def is_alive(self):
        """Return True if health > 0, else False."""
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move alien to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other_object):
        """Placeholder for future collision logic."""
        pass


def new_aliens_collection(positions):
    """Create a list of Alien objects from a list of (x, y) tuples."""
    return [Alien(x, y) for x, y in positions]