from datastore import load_pages_to_datastore, filter_pages_from_datastore
from reverse_index import create_reverse_index, ReverseIndex
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--reverse_index_file",
                        help="if present, program will load given index and run API in sequence.")

    parser.add_argument("--datastore", action='store_true',
                        help="If enabled, a new datastore will be generated")

    parser.add_argument("--filter_data", action='store_true',
                        help="filter pages from filtered_datastore.json")

    parser.add_argument("--create_index", action='store_true',
                        help="Create index using filtered pages from datastore.")

    args = parser.parse_args()

    if not args.reverse_index_file:
        if args.datastore:
            load_pages_to_datastore()

        if args.filter_data:
            filter_pages_from_datastore()

        if args.create_index:
            create_reverse_index()
    else:
        reverse_index = ReverseIndex(args.reverse_index_file)
