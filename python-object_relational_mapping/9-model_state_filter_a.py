#!/usr/bin/python3
"""Lists all State objects containing the letter a from hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main() -> None:
    """Query State objects with 'a' in name, ordered by id, and print them."""
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
        .order_by(State.id)
        .all()
    ):
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    main()
