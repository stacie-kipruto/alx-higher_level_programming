#!/usr/bin/python3
""" List all State objects, and corresponding City
    objects, contained in the database hbtn_0e_101_usa  """

if __name__ == "__main__":

    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
                            @localhost/{sys.argv[3]}", pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
