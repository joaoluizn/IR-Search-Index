from collections import Counter

import json
import os

from utils.file_util import read_json, save_reverse_index_to_json
from utils.text_utils import get_single_page_text, tokenize_text, remove_special_chars

class ReverseIndex:
    def __init__(self,path_to_index):
        if os.path.exists(path_to_index):
            self.path = path_to_index
        else:
            raise Exception("No reverse index file found")
        self.index = self.load_index()

    def load_index(self):
        with open(self.path) as inp_file:
            return json.loads(inp_file.read())

    def get_vocabulary_size(self):
        return len(self.index())


def update_index_dictionary(page_counter, index, doc_id):
    for key in page_counter:
        document_entry = {'id': doc_id, 'frequency': page_counter.get(key)}
        if key not in index:
            index.update({key: [document_entry]})
        else:
            index.update({key: index.get(key) + [document_entry]})

def update_index_tuple(page_counter, index, doc_id):
    for key in page_counter:
        document_entry = (doc_id, page_counter.get(key))
        if key not in index:
            index.update({key: [document_entry]})
        else:
            index.update({key: index.get(key) + [document_entry]})

def update_index_tuple_range(page_counter, index, doc_id):
    for key in page_counter:
        document_entry = (doc_id, page_counter.get(key))
        if key not in index:
            index.update({key: [document_entry]})
        else:
            last_doc_id = index.get(key)[-1][0]
            range_doc = (int(doc_id) - int(last_doc_id))
            new_entry = (range_doc, page_counter.get(key))
            index.update({key: index.get(key) + [new_entry]})

def update_advanced_index_dictionary(field_counter, index, doc_id, field):
    for key in field_counter:
        document_entry = {'id': doc_id, 'frequency': field_counter.get(key)}
        new_key = '{}.{}'.format(key, field)
        if new_key not in index:
            index.update({new_key: [document_entry]})
        else:
            index.update({new_key: index.get(new_key) + [document_entry]})

def update_advanced_index_tuple(field_counter, index, doc_id, field):
    for key in field_counter:
        document_entry = (doc_id, field_counter.get(key))
        new_key = '{}.{}'.format(key, field)
        if new_key not in index:
            index.update({new_key: [document_entry]})
        else:
            index.update({new_key: index.get(new_key) + [document_entry]})

def update_advanced_index_tuple_range(field_counter, index, doc_id, field):
    for key in field_counter:
        document_entry = (doc_id, field_counter.get(key))
        new_key = '{}.{}'.format(key, field)
        if new_key not in index:
            index.update({new_key: [document_entry]})
        else:
            last_doc_id = index.get(new_key)[-1][0]
            range_doc = (int(doc_id) - int(last_doc_id))
            new_entry = (range_doc, field_counter.get(key))
            index.update({new_key: index.get(new_key) + [new_entry]})

def create_reverse_index():
    reverse_index = {}
    json_data = read_json('filtered_datastore.json')
    for data in json_data:
        document_id = data.get('id')
        curr_page_text = get_single_page_text(data)
        clear_text = remove_special_chars(curr_page_text)
        tokenized_page = tokenize_text(clear_text.lower())
        counter = Counter(tokenized_page)
        # update_index_dictionary(counter, reverse_index, document_id)
        # update_index_tuple(counter, reverse_index, document_id)
        # update_index_tuple_range(counter, reverse_index, document_id)
    save_reverse_index_to_json(reverse_index)

def create_advanced_reverse_index():
    reverse_index = {}
    extracted_folder = 'extracted_data'
    for document in sorted(map(int, os.listdir(extracted_folder))):
        document_id = str(document)
        print("Loading file with name: {}".format(document))
        page_data = read_json(os.path.join(extracted_folder, document_id))
        if page_data:
            for key, value in page_data.items():
                field_counter = get_field_counter(value)
                # update_advanced_index_dictionary(field_counter, reverse_index, document, key)
                # update_advanced_index_tuple(field_counter, reverse_index, document, key)
                # update_advanced_index_tuple_range(field_counter, reverse_index, document, key)
    save_reverse_index_to_json(reverse_index, name="advanced_reverse_index_dict.json")

def get_field_counter(value):
    if value:
        if isinstance(value, list):
            value = " ".join(value)
        clear_value = remove_special_chars(value.lower())
        return Counter(clear_value.split(' '))
    return Counter()

