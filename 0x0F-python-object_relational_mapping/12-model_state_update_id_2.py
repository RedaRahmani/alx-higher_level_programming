#!/usr/bin/python3
"""changes the name of a State object"""

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
    ST = ss.query(State).filter(State.id == 2).first()
    ST.name = 'New Mexico'
    ss.commit()
    ss.close()
