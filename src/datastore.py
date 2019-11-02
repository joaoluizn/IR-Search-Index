import os
import shutil

from utils.file_util import create_folder, read_json, save_data_to_json


def load_pages_to_datastore():
    create_folder('page_datastore')
    datastore = []
    counter = 0
    for file in os.listdir('info'):
        if '.json' in file:
            pages_folder_name = '_'.join(file.split('_')[:2])
            pages_folder = os.path.join('pages', pages_folder_name)
            store_objects = read_json(os.path.join('info', file))

            for page_info in store_objects:
                new_file_name = f'{counter}.html'
                source_page = os.path.join(pages_folder, page_info.get('html'))
                destination_page = os.path.join('page_datastore', new_file_name)
                shutil.copy(source_page, destination_page)
                datastore.append({'url': page_info.get('link'),
                                'html': new_file_name, 'id': counter})
                counter += 1
    save_data_to_json(datastore, 'datastore.json')

def filter_pages_from_datastore():
    create_folder('filtered_page_datastore')
    json_datastore = read_json('filtered_datastore.json')

    for page_data in json_datastore:
        source_page = os.path.join("page_datastore", page_data.get('html'))
        destination_page = os.path.join("filtered_page_datastore", page_data.get('html'))
        shutil.copy(source_page, destination_page)

def create_datastore():
    load_pages_to_datastore()
    filter_pages_from_datastore()
