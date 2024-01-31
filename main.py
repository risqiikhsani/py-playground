import greet.greeting
import data.db

# print(greet.greeting.hello("world"))
# print("hello world")
# exec(open("collections/collections.py").read())
# exec(open("arrays/arrays.py").read())

def main():
    try:
        # Connect to the database
        connection = data.db.connect()

        # Create the Person table
        data.db.create_person_table(connection)

        # Run some queries
        # Example:
        # data.db.create_person(connection, "John", 30)
        # data.db.update_person(connection, 1, "Jane", 25)
        # data.db.read_person(connection, 1)
        # data.db.delete_person(connection, 1)

    finally:
        # Close the database connection
        if connection:
            data.db.close_connection(connection)

if __name__ == "__main__":
    main()
