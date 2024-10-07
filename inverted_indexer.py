import re
import json

stop_words = ["the", "and", "is", "in", "it", "of", "to", "a", "that", "with", "for", "as",
    "on", "was", "at", "by", "an", "be", "this", "which", "or", "from", "but",
    "not", "are", "have", "has", "had", "were", "they", "them", "their","you","yours","us","our"]


def indexer(file_path):
    inverted_index = {}
    match = re.search(r'book_(.*)', file_path)
    if match:
        title = match.group(1)

    with open(file_path, 'r', encoding='utf-8') as file:
        print("Book opened")
        content = file.read().lower()
        words = re.findall(r'\b\w+\b', content)
        for word in words:
            books = []
            if word not in stop_words and not word.isdigit():
                books.append(title)
                inverted_index[word] = books
    return inverted_index


def save_inverted_index(inverted_index, output_file):

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(inverted_index, f, ensure_ascii=False, indent=4)