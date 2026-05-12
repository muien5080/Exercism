"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""

    seat_letters = ["A", "B", "C", "D"]

    for i in range(number):
        yield seat_letters[i % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats."""

    row = 1
    generated = 0

    while generated < number:
        # Skip row 13
        if row == 13:
            row += 1
            continue

        for letter in ["A", "B", "C", "D"]:
            if generated >= number:
                return

            yield f"{row}{letter}"
            generated += 1

        row += 1


def assign_seats(passengers):
    """Assign seats to passengers."""

    seats = generate_seats(len(passengers))

    return {
        passenger: next(seats)
        for passenger in passengers
    }


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket."""

    for seat in seat_numbers:
        code = seat + flight_id
        yield code.ljust(12, "0")