from datetime import datetime, timedelta

def first_workday(year, month):
    d = datetime(year, month, 1, 8, 0)
    while d.weekday() >= 5:
        d += timedelta(days=1)
    return d

def last_workday(year, month):
    if month == 12:
        d = datetime(year, 12, 31, 8, 0)
    else:
        d = datetime(year, month + 1, 1, 8, 0) - timedelta(days=1)
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d.replace(hour=8, minute=0, second=0, microsecond=0)

def delivery_date(start, description):
    # 🔑 Convert string to datetime
    start = datetime.fromisoformat(start)

    # FIXED CASES
    if description == "NOW":
        result = start + timedelta(hours=2)

    elif description == "ASAP":
        if start.hour < 13:
            result = start.replace(hour=17, minute=0, second=0, microsecond=0)
        else:
            result = (start + timedelta(days=1)).replace(hour=13, minute=0, second=0, microsecond=0)

    elif description == "EOW":
        weekday = start.weekday()
        if weekday <= 2:  # Mon-Wed
            target = start + timedelta(days=(4 - weekday))
            result = target.replace(hour=17, minute=0, second=0, microsecond=0)
        else:  # Thu-Fri
            target = start + timedelta(days=(6 - weekday))
            result = target.replace(hour=20, minute=0, second=0, microsecond=0)

    # VARIABLE CASES
    elif description.endswith("M"):
        month = int(description[:-1])
        if start.month < month:
            result = first_workday(start.year, month)
        else:
            result = first_workday(start.year + 1, month)

    elif description.startswith("Q"):
        quarter = int(description[1:])
        current_q = (start.month - 1) // 3 + 1
        q_month = quarter * 3

        if current_q <= quarter:
            result = last_workday(start.year, q_month)
        else:
            result = last_workday(start.year + 1, q_month)

    # 🔑 Convert back to string
    return result.isoformat()