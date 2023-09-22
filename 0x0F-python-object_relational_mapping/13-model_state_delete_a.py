#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    ss = Session(engine)
    for ST in ss.query(State).filter(State.name.like('%a%')):
        ss.delete(ST)
    ss.commit()
    ss.close()
