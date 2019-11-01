import os
import json
import shutil
import re
from bs4 import BeautifulSoup

def load_pages_to_datastore():
    create_page_datastore_folder()
    datastore = []
    counter = 0
    for file in os.listdir('info'):
        pages_folder_name = '_'.join(file.split('_')[:2])
        pages_folder = os.path.join('pages', pages_folder_name)
        store_objects = get_pages_from_json_info(file)

        for page_info in store_objects:
            new_file_name = f'{counter}.html'
            source_page = os.path.join(pages_folder, page_info.get('html'))
            destination_page = os.path.join('page_datastore', new_file_name)
            shutil.copy(source_page, destination_page)
            datastore.append({'url': page_info.get('link'), 'html': new_file_name, 'id': counter})
            counter += 1
    create_datastore_info_json(datastore)

def filter_pages_from_datastore():
    create_filtered_page_datastore_folder()
    with open('filtered_datastore.json') as filter_file:
        json_datastore = json.loads(filter_file.read())

    for f in json_datastore:
        source_page = os.path.join("page_datastore", f.get('html'))
        destination_page = os.path.join("filtered_page_datastore", f.get('html'))
        shutil.copy(source_page, destination_page)

def get_page_text(page_content):
    soup = BeautifulSoup(page_content, features="html.parser")
    return soup.get_text()

def create_datastore_info_json(data):
    with open('datastore.json', 'w+') as datastore:
        datastore.write(json.dumps(data, indent=4))

def create_page_datastore_folder():
    if not os.path.isdir('page_datastore'):
        os.mkdir('page_datastore')

def create_filtered_page_datastore_folder():
    if not os.path.isdir('filtered_page_datastore'):
        os.mkdir('filtered_page_datastore')

# File Utils
def read_json(path):
    with open(path) as file:
        return json.loads(file.read())

def get_pages_from_json_info(file_name):
    with open(os.path.join('info', file_name)) as store_json:
        return json.loads(store_json.read())


# Text Utils
def remove_special_chars(text):
    return re.sub(r'[\W_\d]+', ' ', text)

def tokenize_text(text):
    return re.split(r' +', text.strip())

