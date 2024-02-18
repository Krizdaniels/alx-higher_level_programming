#!/usr/bin/python3
"""
A script that changes the name of a State object to the database
Using module SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # To create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # To create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # To create a Session
    session = Session()
    Base.metadata.create_all(engine)
    state_update = session.query(State).filter_by(id='2').first()
    state_update.name = "New Mexico"
    # To commit and close session
    session.commit()
    session.close()
