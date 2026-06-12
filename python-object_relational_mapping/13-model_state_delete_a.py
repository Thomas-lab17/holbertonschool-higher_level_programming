#!/usr/bin/python3
"""Deletes all State objects with a name containing 'a' from hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main() -> None:
    """Delete State records whose name contains the letter 'a'."""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, password, db_name),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in (
        session.query(State)
        .filter(State.name.contains("a"))
        .all()
    ):
        session.delete(state)
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
