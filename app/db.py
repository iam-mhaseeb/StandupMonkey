import sqlite3
from datetime import datetime

CON = sqlite3.connect('standup-monkey.db', check_same_thread=False)
CURSOR = CON.cursor()


def create_tables_in_db():
    """
    Creates required tables.
    :return: None
    """
    CURSOR.execute(
        """
        CREATE TABLE IF NOT EXISTS standups
        (
            user_id     INT,
            date        TEXT,
            yesterday   TEXT,
            today       TEXT,
            blocker     TEXT,
            channel     TEXT,
            modified_at TEXT
        );
        """
    )


def upsert_today_standup_status(user_id, channel, column_name='', message=''):
    """
    Inserts today's standup status to database.
    :param message: Standup message to store
    :param column_name: Column name in which message needs to store
    :return: None
    """
    today = datetime.today().strftime('%Y-%m-%d')
    now = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    CURSOR.execute(
        """
        INSERT INTO standups (
            user_id,
            date,
            {column_name}
            channel,
            modified_at
        )
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(user_id, date) DO UPDATE SET 
            user_id=excluded.user_id,
            date=excluded.date
        ;
        """.format(
            column_name=f'{column_name},' if column_name else ''
        ),
        (user_id, today, message, channel, now)
    )


if __name__ == "__main__":
    create_tables_in_db()
