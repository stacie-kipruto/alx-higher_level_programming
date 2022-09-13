#!/usr/bin/python3
""" Print the first State object from the database hbtn_0e_6_usa """

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
    first = session.query(State).order_by(State.id).first()
    if first:
        print(f"{first.id}: {first.name}")
    else:
        print("Nothing")
    session.close()
