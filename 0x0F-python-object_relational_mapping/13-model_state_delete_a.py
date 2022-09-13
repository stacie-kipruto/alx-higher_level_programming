#!/usr/bin/python3
""" Delete all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.schema import Table


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
                            @localhost/{sys.argv[3]}", pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)
    session.commit()
