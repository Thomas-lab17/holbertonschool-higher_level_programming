#!/usr/bin/python3
"""List cities of a given state from MySQL database."""
import MySQLdb
import sys


def main() -> None:
    """Print city names for the provided state, ordered by city id."""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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
        "SELECT cities.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,),
    )
    rows = cursor.fetchall()
    print(", ".join(row[0] for row in rows))
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
