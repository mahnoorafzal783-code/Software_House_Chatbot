import sqlite3

DATABASE_NAME = "software_house.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Projects table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id TEXT UNIQUE,
            client_name TEXT,
            company_name TEXT,
            service TEXT,
            requirements TEXT,
            budget TEXT,
            timeline TEXT,
            estimated_price TEXT,
            project_status TEXT
        )
    """)

    # Conversations table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id TEXT,
            user_message TEXT,
            ai_response TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_project(
    project_id,
    client_name,
    company_name,
    service,
    requirements,
    budget,
    timeline,
    estimated_price,
    project_status
):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO projects
        (
            project_id,
            client_name,
            company_name,
            service,
            requirements,
            budget,
            timeline,
            estimated_price,
            project_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        project_id,
        client_name,
        company_name,
        service,
        requirements,
        budget,
        timeline,
        estimated_price,
        project_status
    ))

    connection.commit()
    connection.close()


def save_conversation(project_id, user_message, ai_response):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO conversations
        (project_id, user_message, ai_response)
        VALUES (?, ?, ?)
    """, (
        project_id,
        user_message,
        ai_response
    ))

    connection.commit()
    connection.close()


create_database()
def get_conversations(project_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT user_message, ai_response
        FROM conversations
        WHERE project_id = ?
        ORDER BY id
    """, (project_id,))

    conversations = cursor.fetchall()
    connection.close()

    return conversations