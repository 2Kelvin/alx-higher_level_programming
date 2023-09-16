#!/usr/bin/python3
"""Cities in state"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv as a
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == '__main__':
    cnctor = f'mysql+mysqldb://{a[1]}:{a[2]}@localhost:3306/{a[3]}'
    sqlEngine = create_engine(cnctor, pool_pre_ping=True)
    Session = sessionmaker(bind=sqlEngine)
    sesn = Session()
    usCities = sesn.query(City, State).join(State)
    for cty, stte in usCities.all():
        print(f'{stte.name}: ({cty.id}) {cty.name}')
    sesn.commit()
    sesn.close()
