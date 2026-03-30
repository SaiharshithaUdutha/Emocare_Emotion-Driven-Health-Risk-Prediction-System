import sqlite3

# Create table
def create_table():
    conn = sqlite3.connect("emocare.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
    emotion TEXT,
    sleep INTEGER,
    exercise INTEGER,
    junk INTEGER,
    risk TEXT
    )
    """)

    conn.commit()
    conn.close()


# Save data
def save_data(emotion, sleep, exercise, junk, risk):

    conn = sqlite3.connect("emocare.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history VALUES (?,?,?,?,?)",
        (emotion, sleep, exercise, junk, risk)
    )

    conn.commit()
    conn.close()