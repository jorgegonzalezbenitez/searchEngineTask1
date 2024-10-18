import sys
import time
import threading
from SearchingEngine.Crawler.crawler import crawler
from SearchingEngine.Indexer.jsonIndexer import *
from SearchingEngine.Indexer.mongoIndexer import *
from userQuery import *

db_name = "BooksDatabase"
collection_name = "InvertedIndex"
stop_event = threading.Event()

def process_books():
    while not stop_event.is_set():
        crawler()

        dictionary = indexer_json(sys.argv[1])

        save_inverted_index_json(dictionary, sys.argv[2])

        mongo_client, collection = set_connection(db_name, collection_name)

        try:
            dictionary = read_words_from_datalake(sys.argv[1])
            build_and_store_inverted_index(dictionary,db_name,collection_name)

        finally:
            mongo_client.close()
        print("Download and indexing completed")
        time.sleep(15)

def user_query():
    while True:
        command = input("Type 'consult' to look up a word or 'exit' to end the program:\n").strip().lower()

        if command == "consult":
            word = input("What word do you want to look up? ").strip()

            mongo_client, collection = set_connection(db_name, collection_name)

            try:
                results = search_in_mongo_datamart(collection, word)
                print(results)
            finally:
                mongo_client.close()

        elif command == "exit":
            print("Finishing program...")
            stop_event.set()
            break

        else:
            print("Command not recognized. Try again.")

if __name__ == "__main__":
    book_thread = threading.Thread(target=process_books)
    query_thread = threading.Thread(target=user_query)

    book_thread.start()
    query_thread.start()

    query_thread.join()
    book_thread.join()

    print("The program has finished")