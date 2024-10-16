
from SearchingEngine.Runner.userQuery import search_in_json_datamart
from SearchingEngine.Indexer.jsonIndexer import *

datalake_path="C:\\Users\\jorge gonzalez\\Documents\\Tercero 2024-2025\\1er Cuatri\\Big Data\\searchingEngine\\SearchingEngine\\SearchingEngine\\Datalake"
datamartTest = "C:\\Users\\jorge gonzalez\\Documents\\Tercero 2024-2025\\1er Cuatri\\Big Data\\searchingEngine\\SearchingEngine\\SearchingEngine\\tests\\DatamartTest\\jsonDatamartTest.json"

dictionary = indexer_json(datalake_path)
def test_save_inverted_index_Json(benchmark):
    benchmark(lambda: save_inverted_index_json(dictionary, datamartTest))
    print("save_inverted_index completed.")
def test_user_query_Json(benchmark):
    word = "project"
    results = benchmark(lambda: search_in_json_datamart(datamartTest, word))
    print(f"Searched results for the word '{word}': {results}")