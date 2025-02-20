from pymongo import MongoClient

def connect():
    try:
        # Connect to MongoDB
        client = MongoClient("mongodb://root:example@localhost:27017/")
        # db = client["mydatabase"]  # Specify the database name
        print("Connected to MongoDB")
        return client
    except Exception as e:
        print("Error while connecting to MongoDB:", e)
        return None

def create_book_collection(db):
    try:
        if "book" not in db.list_collection_names():
            db.create_collection("book")
            print("Collection 'book' created")
        else:
            print("Collection 'book' already exists")
    except Exception as e:
        print("Error while creating collection 'book':", e)

def db_setup(client):
    if client is not None:
        db = client["mydatabase"]
        create_book_collection(db)

def close_connection(client):
    try:
        if client is not None:
            client.close()
            print("MongoDB connection is closed")
    except Exception as e:
        print("Error while closing MongoDB connection:", e)

if __name__ == "__main__":
    db = connect()
    # Run your MongoDB queries here
    close_connection(db)
