#!/usr/bin/python3
"""List states matching a user-provided name safely from MySQL database."""
import MySQLdb
import sys


def main() -> None:
    """Print rows from `states` where name matches the supplied argument."""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name,
        charset="utf8",
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (searched_name,)
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
