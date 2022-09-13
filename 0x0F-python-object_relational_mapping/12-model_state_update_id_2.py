#!/usr/bin/python3
""" Change the name of a State object
    from the database hbtn_0e_6_usa """

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
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
