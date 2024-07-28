import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  # replace with your MySQL username
            password='your_password'  # replace with your MySQL password
        )
        
        if connection.is_connected():
            print("Connected to MySQL Server")
            
            # Create a cursor object using the connection
            cursor = connection.cursor()
            
            # SQL command to create the database
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store;"
            
            # Execute the SQL command
            cursor.execute(create_db_query)
            
            # Commit the transaction
            connection.commit()
            
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        # Print error message if an exception occurs
        print(f"Error: {e}")
    
    finally:
        if (connection.is_connected()):
            # Close the cursor and connection
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Run the function to create the database
create_database()
