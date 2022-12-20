import os
import json
def load_file(file):
    path = "functions/learn_data/"

    with open(os.path.join(path, file), "r") as f:
        tmp = json.load(f)
        return tmp
        

