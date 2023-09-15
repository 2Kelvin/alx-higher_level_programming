#!/usr/bin/python3
"""Cities by states"""
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
    queryCities = 'SELECT id, name, states.name FROM cities \
        JOIN states ON state_id=states.id ORDER BY id'
    cursr.execute(queryCities)
    for row in cursr.fetchall():
        print(row)
    cursr.close()
    dbConnection.close()
