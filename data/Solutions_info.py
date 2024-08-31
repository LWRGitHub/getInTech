import json

class Solutions_info:

    def __init__(self):
        f = open('data/formated_data.json', 'r')
        data = json.load(f)
        f.close()
        self.solutions_info = data

