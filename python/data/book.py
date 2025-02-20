
def create_book(collection, title, author):
    try:
        book_data = {"title": title, "author": author}
        result = collection.insert_one(book_data)
        print("Book inserted with ID:", result.inserted_id)
        return result.inserted_id
    except Exception as e:
        print("Error while creating book:", e)

def read_book(collection, book_id):
    try:
        book = collection.find_one({"_id": book_id})
        if book:
            print("Book found:", book)
        else:
            print("Book with ID", book_id, "not found")
    except Exception as e:
        print("Error while reading book:", e)

def update_book(collection, book_id, title, author):
    try:
        update_data = {"$set": {"title": title, "author": author}}
        result = collection.update_one({"_id": book_id}, update_data)
        print("Updated", result.modified_count, "book(s)")
    except Exception as e:
        print("Error while updating book:", e)

def delete_book(collection, book_id):
    try:
        result = collection.delete_one({"_id": book_id})
        print("Deleted", result.deleted_count, "book(s)")
    except Exception as e:
        print("Error while deleting book:", e)

