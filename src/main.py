from datastore import load_pages_to_datastore, filter_pages_from_datastore
from reverse_index import create_reverse_index, ReverseIndex, create_advanced_reverse_index
import argparse

from flask import Flask
app = Flask(__name__)
reverse_index = None
advanced_reverse_index = None

@app.route('/')
def hello_world():
    return 'Hello, Index!!'

@app.route('/search-adv')
def adv_search_game():
    return 'Search game stub endpoint. Adv index len: {}'.format(len(advanced_reverse_index.index))

@app.route('/search')
def simple_search_game():
    return 'Search game stub endpoint. Adv index len: {}'.format(len(reverse_index.index))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--reverse_index_file",
                        help="if present, program will load given index and run API in sequence.")

    parser.add_argument("--reverse_index_advanced_file",
                        help="if present, program will load given index and run API in sequence.")

    parser.add_argument("--datastore", action='store_true',
                        help="If enabled, a new datastore will be generated")

    parser.add_argument("--filter_data", action='store_true',
                        help="filter pages from filtered_datastore.json")

    parser.add_argument("--create_index", action='store_true',
                        help="Create index using filtered pages from datastore.")

    parser.add_argument("--create_advance_index", action='store_true',
                        help="Create advanced index using extracted data from datastore pages.")

    args = parser.parse_args()

    if not args.reverse_index_file or args.reverse_index_advanced_file:
        if args.datastore:
            load_pages_to_datastore()

        if args.filter_data:
            filter_pages_from_datastore()

        if args.create_index:
            create_reverse_index()

        if args.create_advance_index:
            create_advanced_reverse_index()

    if args.reverse_index_file and args.reverse_index_advanced_file:
        reverse_index = ReverseIndex(args.reverse_index_file)
        advanced_reverse_index = ReverseIndex(args.reverse_index_advanced_file)
        app.run(debug=True)
    elif args.reverse_index_file:
        reverse_index = ReverseIndex(args.reverse_index_file)
        app.run(debug=True)
    elif args.reverse_index_advanced_file:
        advanced_reverse_index = ReverseIndex(args.reverse_index_advanced_file)
        app.run(debug=True)
