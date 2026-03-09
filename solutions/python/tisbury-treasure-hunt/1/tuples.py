# 1. Extract coordinate from Azara's record
def get_coordinate(record):
    return record[1]


# 2. Convert "2A" → ("2", "A")
def convert_coordinate(coordinate):
    return (coordinate[0], coordinate[1])


# 3. Compare coordinates from both records
def compare_records(azara_record, rui_record):
    azara_coord = convert_coordinate(get_coordinate(azara_record))
    rui_coord = rui_record[1]

    return azara_coord == rui_coord


# 4. Create combined record if coordinates match
def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        treasure = azara_record[0]
        coordinate = azara_record[1]
        location = rui_record[0]
        rui_coordinate = rui_record[1]
        quadrant = rui_record[2]

        return (treasure, coordinate, location, rui_coordinate, quadrant)
    else:
        return "not a match"


# 5. Clean up records and produce report
def clean_up(combined_records):
    report = ""

    for record in combined_records:
        cleaned = (record[0], record[2], record[3], record[4])
        report += str(cleaned) + "\n"

    return report