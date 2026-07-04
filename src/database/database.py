import sqlite3

DB_NAME = "phishing_history.db"


def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            scan_type TEXT,

            input_data TEXT,

            prediction TEXT,

            risk TEXT,

            score REAL,

            scan_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)

    conn.commit()

    conn.close()


def insert_record(scan_type,
                  input_data,
                  prediction,
                  risk,
                  score):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO history(

        scan_type,

        input_data,

        prediction,

        risk,

        score

        )

        VALUES(?,?,?,?,?)

    """,

    (

        scan_type,

        input_data,

        prediction,

        risk,

        score

    )

    )

    conn.commit()

    conn.close()


def get_history():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM history

        ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data