import os
import re
from bs4 import BeautifulSoup

def get_page_text(page_content):
    soup = BeautifulSoup(page_content, features="html.parser")
    return soup.get_text()

def get_single_page_text(page_data):
    with open(os.path.join('filtered_page_datastore', page_data.get('html'))) as page:
        return get_page_text(page.read())

def remove_special_chars(text):
    return re.sub(r'[\W_\d]+', ' ', text)

def tokenize_text(text):
    return re.split(r' +', text.strip())

