"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons."""
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons."""
    # Move first two to end
    first, second, *rest = each_wagons_id

    # Find locomotive (1) and insert missing wagons after it
    # First reconstruct list after moving
    reordered = [*rest, first, second]

    # Unpack to place missing wagons after locomotive
    loco, *others = reordered
    return [loco, *missing_wagons, *others]


def add_missing_stops(route, **stops):
    """Add missing stops to route dict."""
    # Sort stops by key to maintain order: stop_1, stop_2, ...
    ordered_stops = [value for key, value in sorted(stops.items())]
    return {**route, "stops": ordered_stops}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information."""
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons."""
    # Unpack rows
    row1, row2, row3 = wagons_rows

    # Transpose rows into columns using unpacking + zip
    fixed = list(zip(row1, row2, row3))

    # Convert tuples of tuples into required list format
    return [list(group) for group in fixed]