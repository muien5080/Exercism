# Directions
NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'

# Turning maps
RIGHT_TURN = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH
}

LEFT_TURN = {
    NORTH: WEST,
    WEST: SOUTH,
    SOUTH: EAST,
    EAST: NORTH
}

# Advancing map
ADVANCE_MOVE = {
    NORTH: (0, 1),
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0)
}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)  # Use coordinates tuple to match tests

    def turn_right(self):
        self.direction = RIGHT_TURN[self.direction]

    def turn_left(self):
        self.direction = LEFT_TURN[self.direction]

    def advance(self):
        dx, dy = ADVANCE_MOVE[self.direction]
        x, y = self.coordinates
        self.coordinates = (x + dx, y + dy)

    def move(self, instructions):
        """Execute a string of instructions: R, L, A"""
        for instr in instructions:
            if instr == 'R':
                self.turn_right()
            elif instr == 'L':
                self.turn_left()
            elif instr == 'A':
                self.advance()
            else:
                raise ValueError(f"Unknown instruction: {instr}")