
def laod_data_from_std(path): # lade standart daten | (gibt keine möglichkeit zur änderung nur lesen)
    content = []
    with open(path) as file:
        for x in file.readline():
            content.append(x)
    return content