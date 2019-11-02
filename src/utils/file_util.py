import os
import json

def save_data_to_json(data, path):
    """ Save data to a created json """
    with open(path, 'w') as datastore:
        datastore.write(json.dumps(data, indent=4))

def read_json(path):
    """ Read Json data and parse data to object """
    with open(path) as file:
        return json.loads(file.read())

def create_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

def save_reverse_index_to_json(index):
    with open('single_term_index.json', 'w+') as reverse:
        reverse.write(json.dumps(index, indent=4, ensure_ascii=True))

