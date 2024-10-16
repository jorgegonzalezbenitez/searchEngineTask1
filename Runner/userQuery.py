import json


def search_in_json_datamart(json_file_path, word):
    try:

        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if word in data:
            results = data[word]
            return format_results_json(results)
        else:
            return f"No results were found for the word '{word}' in the JSON datamart."
    except FileNotFoundError:
        return f"File {json_file_path} was not found."
    except Exception as e:
        return f"An error occurred: {e}"


def search_in_mongo_datamart(collection, word):

    word = str(word).lower().strip()

    cursor = collection.find({"_id": word})

    if not collection.find({"_id": word}):
        return f"No results were found for the word '{word}' in Mongo Database."

    output = ""
    for result in cursor:

        for book in result.get("Books", []):
            output += f"\nTitle: {book.get('title', 'Unknown')}\n"
            output += f"Author: {book.get('author', 'Unknown')}\n"
            output += f"Language: {book.get('language', 'Unknown')}\n"
            output += f"Released Date: {book.get('release_date', 'Unknown')}\n"
            output += "-" * 40 + "\n"

    return output.strip()

def format_results_json(results):
    output = ""
    for book in results:
        output += f"\nTitle: {book.get('title', 'Unknown')}\n"
        output += f"Author: {book.get('author', 'Unknown')}\n"
        output += f"Language: {book.get('language', 'Unknown')}\n"
        output += f"Released Date: {book.get('release_date', 'Unknown')}\n"
        output += "-" * 40 + "\n"
    return output.strip()
