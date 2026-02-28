cc = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    f = cc.index(colors[0])
    s = cc.index(colors[1])
    return f * 10 + s