import sqlite3
import os

def delete_table(table_name, db_path):
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Delete the specified table if it exists
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        conn.commit()
        print(f"{table_name} table deleted successfully!")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Unexpected error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    db_path = os.path.join(parent_dir, 'video_database.db')
    delete_table('videos', db_path)