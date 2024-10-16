import os
import re
from pymongo import MongoClient

stop_words = ["the", "and", "is", "in", "it", "of", "to", "a", "that", "with", "for", "as",
              "on", "was", "at", "by", "an", "be", "this", "which", "or", "from", "but",
              "not", "are", "have", "has", "had", "were", "they", "them", "their", "you",
              "yours", "us", "our"]

def extract_metadata(content):
    title_match = re.search(r'Title:\s*(.*)', content)
    author_match = re.search(r'Author:\s*(.*)', content)
    release_date_match = re.search(r'Release date:\s*(.*)', content)
    language_match = re.search(r'Language:\s*(.*)', content)

    title = title_match.group(1) if title_match else "Unknown"
    author = author_match.group(1) if author_match else "Unknown"
    release_date = release_date_match.group(1) if release_date_match else "Unknown"
    language = language_match.group(1) if language_match else "Unknown"

    return title, author, release_date, language


def set_connection(db_name, collection_name):
    mongo_client = MongoClient('mongodb://localhost:27017/')
    db = mongo_client[db_name]
    collection = db[collection_name]
    return mongo_client, collection


def read_words_from_datalake(datalake_path):
    inverted_dict = {}

    for filename in os.listdir(datalake_path):
        if filename.startswith("book_") and filename.endswith(".txt"):
            file_path = os.path.join(datalake_path, filename)

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    title, author, release_date, language = extract_metadata(content)

                    book_entry = {
                        "title": title,
                        "author": author,
                        "release_date": release_date,
                        "language": language
                    }

                    words = re.findall(r'\b\w+\b', content.lower())
                    for word in words:
                        if word not in stop_words and not word.isdigit():
                            if word not in inverted_dict:
                                inverted_dict[word] = []
                            if book_entry not in inverted_dict[word]:
                                inverted_dict[word].append(book_entry)
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

    return inverted_dict


def build_and_store_inverted_index(inverted_dict, db_name, collection_name):

    mongo_client, collection = set_connection(db_name, collection_name)


    try:
        for word, books in inverted_dict.items():
            collection.update_one(
                {"_id": word},
                {"$addToSet": {"Books": {"$each": books}}},
                upsert=True
            )
    except Exception as e:
        print(f"Error storing the inverted index in MongoDB: {e}")
        raise
    finally:
        mongo_client.close()