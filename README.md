# IR-Search-Index
Information Retrieval Search Index project.

# Assemble datastore.json
The datastore.json is a file containing all references to downloaded html files, plus an ID and page URL.

- Put all info `json` files inside `info` folder.

- Put all `store folders`, containing every downloaded `html` for that store, inside `pages` folder.

After everything is setted, run the following command:

```shell
$ python main.py --datastore
```

# Filter pages from relevace file

Download the `filtered_datastore.json` and put it within the `src` folder.

After that, just run the following command on terminal:

```
$ python main.py --filter_data
```

# Create Index

Now that every filtered relevant pages are located in the `filtered_page_datastore` folder, run the following command to build the reverse index:

```
$ python main.py --create_index
```

# Setup existent Index
If you have access to an Index file previously generated, just download one of the following index files:

- single_term_index_dict.json
- single_term_index_tuple.json
- single_term_index_reduced.json

Place it within `src` folder

Run the following:

```shell
$ python main.py --reverse_index_file="<index_file_name>"
```

This should load existent index and run the flask server.

Thanks for your time!