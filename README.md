# MongoDB Operations with Python and PyMongo

This repository contains Python code demonstrating various **MongoDB operations** using the **PyMongo** library. The code is organized into two main directories:

- **AGGREGATIONS**: This folder contains examples of MongoDB aggregation operations such as `match`, `group`, `sort`, and `project`.
- **CRUD_OPERATIONS**: This folder contains basic CRUD (Create, Read, Update, Delete) operations and transactions using MongoDB.

## Project Structure

```
/
├── AGGREGATIONS/
│   ├── match_group.py           # Example of aggregation using $match and $group
│   └── sort_project.py          # Example of aggregation using $sort and $project
│
└── CRUD_OPERATIONS/
    ├── delete.py                # Example of deleting documents
    ├── find.py                  # Example of finding documents
    ├── insert.py                # Example of inserting documents
    ├── transactions.py          # Example of transactions in MongoDB
    └── update.py                # Example of updating documents
```

## Description of the Folders

### AGGREGATIONS

The **AGGREGATIONS** folder contains two examples of aggregation pipelines used to manipulate and analyze data in MongoDB.

1. **match_group.py**:
    - Demonstrates the use of the `$match` and `$group` stages in an aggregation pipeline.
    - `$match` is used to filter documents, while `$group` is used to group documents based on a specified field and perform specific operations such as counting or summing.

2. **sort_project.py**:
    - Demonstrates the use of the `$sort` and `$project` stages in an aggregation pipeline.
    - `$sort` is used to sort documents by a specified field (1: from highest to lowest, 0: the opposite), and `$project` is used to include or exclude specific fields from the results.

### CRUD_OPERATIONS

The **CRUD_OPERATIONS** folder contains five files, each demonstrating a different basic operation in MongoDB:

1. **delete.py**:
    - Demonstrates how to delete documents from a MongoDB collection using the `delete_one()` and `delete_many()` methods.

2. **find.py**:
    - Demonstrates how to find documents in a MongoDB collection using the `find_one()` and `find()` method.

3. **insert.py**:
    - Demonstrates how to insert documents into a MongoDB collection using the `insert_one()` and `insert_many()` methods.

4. **transactions.py**:
    - Demonstrates how to perform transactions in MongoDB using the `start_session()` method and multi-document transactions.

5. **update.py**:
    - Demonstrates how to update documents in a MongoDB collection using the `update_one()` and `update_many()` methods.

## Requirements

To run this code, you need the following Python packages:

- **PyMongo**: To interact with MongoDB from Python.

You can install the required packages using pip:

```bash
pip install pymongo
```

