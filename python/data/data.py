import psycopg2
import csv

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS example_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
    """)

def insert_data_from_csv(cursor, csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            cursor.execute(
                "INSERT INTO example_table (name, age) VALUES (%s, %s)",
                (row[0], int(row[1]))
            )

def main():
    # PostgreSQL connection parameters
    dbname = 'your_database_name'
    user = 'your_username'
    password = 'your_password'
    host = 'your_host'  # Usually 'localhost' if the database is hosted locally
    port = 'your_port'  # Usually '5432' for PostgreSQL

    # CSV file path
    csv_file = 'your_csv_file.csv'

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cursor = conn.cursor()

    # Create table if not exists
    create_table(cursor)

    # Insert data from CSV file
    insert_data_from_csv(cursor, csv_file)

    # Commit the transaction and close the cursor and connection
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
