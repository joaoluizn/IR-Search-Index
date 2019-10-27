import os
import json
import shutil

def load_pages_to_datastore():
    create_page_datastore_folder()
    datastore = []
    counter = 0
    for file in os.listdir('info'):
        pages_folder_name = '_'.join(file.split('_')[:2])
        pages_folder = os.path.join('pages', pages_folder_name)
        store_objects = get_pages_from_json(file)

        for page_info in store_objects:
            new_file_name = f'{counter}.html'
            source_page = os.path.join(pages_folder, page_info.get('html'))
            destination_page = os.path.join('page_datastore', new_file_name)
            shutil.copy(source_page, destination_page)
            datastore.append({'url': page_info.get('link'), 'html': new_file_name, 'id': counter})
            counter += 1
    create_datastore_info_json(datastore)


def get_pages_from_json(file_name):
    with open(os.path.join('info', file_name)) as store_json:
        return json.loads(store_json.read())

def create_datastore_info_json(data):
    with open('datastore.json', 'w+') as datastore:
        datastore.write(json.dumps(data, indent=4))

def create_page_datastore_folder():
    if not os.path.isdir('page_datastore'):
        os.mkdir('page_datastore')
