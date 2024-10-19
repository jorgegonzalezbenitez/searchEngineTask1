# Task 1: Python Search Engine

## University of Las Palmas de Gran Canaria
### School of Computer Engineering
#### Bachelor's Degree in Data Science and Engineering

---

## Description

This project implements a search engine that interacts with [Project Gutenberg](https://www.gutenberg.org/) to periodically download books, storing them in a local datalake. The functionality for retrieving and storing these books is handled by the **Crawler** module.

Once the books are collected, the **Indexer** module processes the content and builds two types of inverted indexes, which serve as two datamarts: 
1. **JSON-based Index**: A static file-based approach.
2. **MongoDB-based Index**: A dynamic, scalable NoSQL database.

The **Runner** module provides a user interface, enabling users to search for a specific word across the two inverted indexes. Users can choose whether to query the JSON-based or MongoDB-based index for their search.

In addition, the project includes a **Benchmarking** module that compares the performance of both index types. It uses benchmark tests to evaluate:
- Query execution time in both systems.
- The efficiency of storing the inverted index in JSON versus MongoDB.

---

## Resources

This project was developed using the following tools:

- **[PyCharm](https://www.jetbrains.com/pycharm/)**: An integrated development environment (IDE) designed specifically for Python. It offers a wide range of features for efficient code writing, debugging, and testing.
  
- **[MongoDB](https://www.mongodb.com/)**: A NoSQL database used for its high performance and scalability in storing large datasets, such as the inverted index.

- **[Pytest](https://docs.pytest.org/)**: A testing framework utilized to run benchmark tests that compare the performance of MongoDB and JSON for storing and querying inverted indexes.

- **[Project Gutenberg](https://www.gutenberg.org/)**: A digital library that provides free access to public domain eBooks, which are used as the data source for the search engine.

---

## Benchmarking Results

![Pytest Results](![WhatsApp Image 2024-10-16 at 20 12 26](https://github.com/user-attachments/assets/d90d4b33-8b7e-4b95-a20d-22e81f871d57)
)

The benchmarking tests revealed the following insights:

- **Query Performance**: MongoDB significantly outperforms the JSON file in query execution (as seen in the `test_user_query_Mongo` benchmark). This makes MongoDB highly efficient for search queries, especially in large datasets.
  
- **Storage Performance**: The process of saving the inverted index to MongoDB (`test_save_inverted_index_Mongo`) is slower than saving it to JSON. This suggests that while MongoDB excels at querying, it incurs a performance cost when handling bulk data inserts like inverted indexes.
  
- **Overall**: MongoDB is ideal for environments where fast query response times are critical. However, JSON may still be preferred in scenarios where the primary concern is minimizing the time spent storing data rather than querying it.

---

## Tools and Libraries

- **[MongoDB](https://www.mongodb.com/)**: Used for building a scalable, document-oriented database for the inverted index.
- **[Pytest](https://docs.pytest.org/)**: Employed for testing and benchmarking.
- **[Project Gutenberg](https://www.gutenberg.org/)**: Source of the eBook data.
