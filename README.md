# EcoApi
Python API for language processing from grocery receipts

## Project Overview
This Django-based project implements a fuzzy matching algorithm to identify and retrieve detailed information about products from a given text input. It's designed to handle queries such as product names from receipts or inventory lists, matching them against a pre-defined product dictionary to return comprehensive metadata.
## Key Features
Fuzzy Matching: Utilizes the fuzzywuzzy Python library to find the closest match to a given product name within a list of known products.
Product Dictionary: A rich dictionary containing detailed metadata about each product, including ID, food category, expected shelf life, storage method, and more.
Django API Endpoint: A simple and efficient Django setup that offers an API endpoint for product name queries and returns matched product details.
## How It Works
Fuzzy Matching Logic: The system takes a product name as input and performs fuzzy matching against known product names. It is capable of handling single-word products like "bananas" as well as multi-word items such as "green beans".
Product Metadata Retrieval: Upon finding the best match, the system retrieves the full metadata entry from the product dictionary, providing comprehensive details about the product.
Django Endpoint: The functionality is exposed through a Django API endpoint, allowing easy integration with front-end applications or other services.
## Technologies Used
Python
Django
FuzzyWuzzy Python Library
Python-Levenshtein (optional for performance improvement)


https://python-eco.fly.dev/items