#!/usr/bin/python3
"""List all states from the specified MySQL database."""
import MySQLdb
import sys


def main() -> None:
    """Print all rows from the states table ordered by id."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8",
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
