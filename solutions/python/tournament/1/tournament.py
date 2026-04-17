def tally(rows):
    table = {}

    def ensure_team(team):
        if team not in table:
            table[team] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

    for row in rows:
        if not row.strip():
            continue

        team1, team2, result = row.split(";")

        ensure_team(team1)
        ensure_team(team2)

        table[team1]["MP"] += 1
        table[team2]["MP"] += 1

        if result == "win":
            table[team1]["W"] += 1
            table[team1]["P"] += 3
            table[team2]["L"] += 1

        elif result == "loss":
            table[team2]["W"] += 1
            table[team2]["P"] += 3
            table[team1]["L"] += 1

        elif result == "draw":
            table[team1]["D"] += 1
            table[team2]["D"] += 1
            table[team1]["P"] += 1
            table[team2]["P"] += 1

    sorted_teams = sorted(
        table.items(),
        key=lambda item: (-item[1]["P"], item[0])
    )

    lines = ["Team                           | MP |  W |  D |  L |  P"]

    for team, stats in sorted_teams:
        lines.append(
            f"{team:<31}| {stats['MP']:>2} | {stats['W']:>2} | {stats['D']:>2} | {stats['L']:>2} | {stats['P']:>2}"
        )

    return lines