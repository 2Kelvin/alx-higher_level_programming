#!/usr/bin/python3
"""All cities by state"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    dbConnection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursr = dbConnection.cursor()
    queryCities = 'SELECT cities.name FROM cities JOIN \
        states ON cities.state_id=states.id WHERE states.name \
             LIKE BINARY %(arg)s ORDER BY cities.id', {'arg': argv[4]}
    cursr.execute(queryCities)
    for row in cursr.fetchall():
        print(row)
    cursr.close()
    dbConnection.close()
