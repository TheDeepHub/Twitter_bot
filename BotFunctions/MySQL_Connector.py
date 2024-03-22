import os 
from dotenv import load_dotenv

import mysql.connector
from mysql.connector import Error


# Load the environment variables

load_dotenv()

mySQL_database = os.getenv("MYSQL_DATABASE")
mySQL_password = os.getenv("MYSQL_PASSWORD")
mySQL_host = os.getenv("MYSQL_HOST")
mySQL_user = os.getenv("MYSQL_USER")

def insert_article(title, author, abstract, publication_date, url, keywords, summary):
    try:
        conn = mysql.connector.connect(
            host=mySQL_host,
            user=mySQL_user,
            password=mySQL_password,
            database=mySQL_database
        )
        cursor = conn.cursor()

        # Use the INSERT query as before, now publication_date is directly a string
        insert_query = """
        INSERT INTO papers (title, author, abstract, publication_date, url, keywords, summary)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (title, author, abstract, publication_date, url, keywords, summary))
        
        conn.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
