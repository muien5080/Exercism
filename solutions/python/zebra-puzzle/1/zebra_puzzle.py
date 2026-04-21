from itertools import permutations

def drinks_water():
    return solve()[0]

def owns_zebra():
    return solve()[1]

def solve():
    houses = [1, 2, 3, 4, 5]

    orderings = list(permutations(houses))

    for (red, green, ivory, yellow, blue) in orderings:
        if green != ivory + 1:
            continue

        for (englishman, spaniard, ukrainian, norwegian, japanese) in orderings:
            if englishman != red:
                continue
            if norwegian != 1:
                continue
            if abs(norwegian - blue) != 1:
                continue

            for (dog, snails, fox, horse, zebra) in orderings:
                if spaniard != dog:
                    continue

                for (coffee, tea, milk, oj, water) in orderings:
                    if coffee != green:
                        continue
                    if ukrainian != tea:
                        continue
                    if milk != 3:
                        continue

                    for (dancing, painter, reading, football, chess) in orderings:
                        if snails != dancing:
                            continue
                        if yellow != painter:
                            continue
                        if abs(reading - fox) != 1:
                            continue
                        if abs(painter - horse) != 1:
                            continue
                        if football != oj:
                            continue
                        if japanese != chess:
                            continue

                        # If all constraints pass:
                        nationality = {
                            englishman: "Englishman",
                            spaniard: "Spaniard",
                            ukrainian: "Ukrainian",
                            norwegian: "Norwegian",
                            japanese: "Japanese"
                        }

                        return nationality[water], nationality[zebra]