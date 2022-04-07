import os


def get_week_days():

    singles = list()
    doubles = list()

    for file in os.listdir('./data/single'):
        if (file.endswith('.html')):
            singles.append(os.path.join("./data/single", file))

    for file in os.listdir('./data/double'):
        if (file.endswith('.html')):
            doubles.append(os.path.join("./data/double", file))

    return {"singles": singles, "doubles": doubles}
