from crawler import crawler
import schedule
import time
from inverted_indexer import indexer, save_inverted_index

if __name__ == "__main__":
    #schedule.every(15).seconds.do(crawler)

    #while True:
    #    schedule.run_pending()
    #    time.sleep(1)
    dictionary = indexer("C:\\Users\\aadel\\Desktop\\GCID\\Tercero"
                                  "\\BD\\Task1\\Datalake\\book_The United States Constitution.txt")
    print(dictionary)
    save_inverted_index(dictionary, "C:\\Users\\aadel\\Desktop\\GCID\\Tercero\\BD\\Task1\\Datamart\\hola.json")
