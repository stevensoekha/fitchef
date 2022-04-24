import os


def get_week_days():

    singles = list()
    doubles = list()

    for file in filter(lambda file: file.endswith('.html'), os.listdir('./data')):
        if ('s' in file):
            singles.append(os.path.join("./data", file))
        else:
            doubles.append(os.path.join("./data", file))

    return {"singles": singles, "doubles": doubles}
