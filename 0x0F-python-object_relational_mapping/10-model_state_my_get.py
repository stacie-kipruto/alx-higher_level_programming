#!/usr/bin/python3
""" Print the State object with the name passed
    as argument from the database hbtn_0e_6_usa """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:\
                            {sys.argv[2]}@localhost/{sys.argv[3]}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    session.close()
