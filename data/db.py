import psycopg2

def connect():
    try:
        connection = psycopg2.connect(
            user="myuser",
            password="mypassword",
            host="localhost",
            port="5432",
            database="pyplayground"
        )
        print("Connected to PostgreSQL")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

def create_person_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = 'person')")
        table_exists = cursor.fetchone()[0]
        if not table_exists:
            cursor.execute("""
                CREATE TABLE person (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    age INT NOT NULL
                )
            """)
            print("Created Person table")
        else:
            print("Person table already exists")
        connection.commit()  # Commit changes to the database
    except (Exception, psycopg2.Error) as error:
        print("Error while creating Person table:", error)

def close_connection(connection):
    try:
        if connection is not None:
            connection.close()
            print("PostgreSQL connection is closed")
    except (Exception, psycopg2.Error) as error:
        print("Error while closing PostgreSQL connection", error)

if __name__ == "__main__":
    connection = connect()
    if connection:
        create_person_table(connection)
        # Run other queries here
        # Remember to commit changes and close the connection when done
        close_connection(connection)
