import greet.greeting
import data.db
import data.db2
import data.person
import data.book

# print(greet.greeting.hello("world"))
# print("hello world")
# exec(open("collections/collections.py").read())
# exec(open("arrays/arrays.py").read())



def testdb1():
    try:
        # Connect to the database
        connection = data.db.connect()

        # Create the Person table
        data.db.create_person_table(connection)

        # Run some queries
        # Example:
        data.person.create_person(connection, "John", 30)
        data.person.update_person(connection, 1, "Jane", 25)
        data.person.read_person(connection, 1)
        data.person.delete_person(connection, 1)

    finally:
        # Close the database connection
        if connection is not None:
            data.db.close_connection(connection)

def testdb2():
    try:
        # Connect to the database
        connection = data.db2.connect()
        data.db2.db_setup(connection)

        db = connection["mydatabase"]
        collection = db["book"]
        id = data.book.create_book(collection,"Math","Person1")
        data.book.read_book(collection, id)
        data.book.update_book(collection, id, "New Title", "New Author")
        data.book.delete_book(collection, id)


    finally:
        # Close the database connection
        if connection is not None:
            data.db2.close_connection(connection)

def main():
    testdb1()
    testdb2()

if __name__ == "__main__":
    main()
