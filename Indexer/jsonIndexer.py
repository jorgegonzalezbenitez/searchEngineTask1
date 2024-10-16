import re
import json
import os

stop_words = ["the", "and", "is", "in", "it", "of", "to", "a", "that", "with", "for", "as",
    "on", "was", "at", "by", "an", "be", "this", "which", "or", "from", "but",
    "not", "are", "have", "has", "had", "were", "they", "them", "their","you","yours","us","our"]

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

def indexer_json(datalake_path, inverted_index=None):

    if inverted_index is None:
        inverted_index = {}


    for filename in os.listdir(datalake_path):
        if filename.startswith("book_") and filename.endswith(".txt"):
            file_path = os.path.join(datalake_path, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()


                title, author, release_date, language = extract_metadata(content)

                words = re.findall(r'\b\w+\b', content.lower())

                for word in words:
                    if word not in stop_words and not word.isdigit():
                        if word not in inverted_index:
                            inverted_index[word] = []

                        entry = {
                            "title": title,
                            "author": author,
                            "release_date": release_date,
                            "language": language
                        }

                        if entry not in inverted_index[word]:
                            inverted_index[word].append(entry)

    return inverted_index

def save_inverted_index_json(inverted_index, output_file):

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(inverted_index, f, ensure_ascii=False, indent=4)

