#!/usr/bin/python3
"""List all states from the specified MySQL database."""
import MySQLdb
import sys


def main() -> None:
    """Print all rows from the `states` table ordered by id."""
    user: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]

    db = MySQLdb.connect(host="localhost", 
                         port=3306,
                         user=user, 
                         passwd=password, 
                         db=db_name,
                         charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

