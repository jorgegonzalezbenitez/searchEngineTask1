from SearchingEngine.Indexer.mongoIndexer import *
from SearchingEngine.Runner.userQuery import search_in_mongo_datamart

db_name = "BooksDatabaseTest"
collection_name = "InvertedIndexTest"

datalake_path="C:\\Users\\jorge gonzalez\\Documents\\Tercero 2024-2025\\1er Cuatri\\Big Data\\searchingEngine\\SearchingEngine\\SearchingEngine\\Datalake"

dictionary = read_words_from_datalake(datalake_path)
def test_save_inverted_index_Mongo( benchmark):
    mongo_client, collection = set_connection(db_name, collection_name)

    try:
        benchmark(lambda: build_and_store_inverted_index(dictionary,db_name,collection_name))
        print("Indexación completada")
    finally:
        mongo_client.close()
def test_user_query_Mongo(benchmark):
    word = "project"
    mongo_client,collection = set_connection(db_name, collection_name)
    results = benchmark(lambda: search_in_mongo_datamart(collection, word))
    print(f"Searched results for the word '{word}': {results}")
