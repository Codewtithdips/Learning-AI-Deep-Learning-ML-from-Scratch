import pandas as pd
import mysql.connector
import os  # Added for path handling

# Function to connect Database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345612",
        database="ecommerce"
    )

def run_query_and_save(sql_query, csv_name):
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        df = pd.DataFrame(rows, columns=columns)

        # Save inside "DataSets" folder
        datasets_path = os.path.join(os.path.dirname(__file__), "DataSets", csv_name)
        df.to_csv(datasets_path, index=False)

        print(f"Data saved to: {datasets_path}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    question_heading = input("Enter the question heading : ")
    print(question_heading)

    print("Enter your SQL query (press Enter twice to finish):")
    sql_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        sql_lines.append(line)
    sql_query = "\n".join(sql_lines)

    # Take CSV filename (only filename, no path)
    csv_name = input("Enter the CSV filename to save (e.g., output.csv): ")

    # Run the query and save to CSV
    run_query_and_save(sql_query, csv_name)
