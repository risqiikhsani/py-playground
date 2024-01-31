import psycopg2

def create_person(connection, name, age):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO person (name, age) 
            VALUES (%s, %s) RETURNING id;
        """, (name, age))
        new_person_id = cursor.fetchone()[0]
        connection.commit()  # Commit changes to the database
        print("Created person with ID:", new_person_id)
        return new_person_id
    except (Exception, psycopg2.Error) as error:
        print("Error while creating person:", error)
        return None

def read_person(connection, person_id):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM person WHERE id = %s;", (person_id,))
        person = cursor.fetchone()
        if person:
            print("Person found:", person)
            return person
        else:
            print("Person with ID", person_id, "not found")
            return None
    except (Exception, psycopg2.Error) as error:
        print("Error while reading person:", error)
        return None

def update_person(connection, person_id, name, age):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE person 
            SET name = %s, age = %s 
            WHERE id = %s;
        """, (name, age, person_id))
        connection.commit()  # Commit changes to the database
        print("Updated person with ID:", person_id)
    except (Exception, psycopg2.Error) as error:
        print("Error while updating person:", error)

def delete_person(connection, person_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM person WHERE id = %s;", (person_id,))
        connection.commit()  # Commit changes to the database
        print("Deleted person with ID:", person_id)
    except (Exception, psycopg2.Error) as error:
        print("Error while deleting person:", error)