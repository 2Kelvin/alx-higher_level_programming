#!/usr/bin/python3
"""Filter states"""
import MySQLdb
from sys import argv


def filterStates(argUser, argPswd, argDbName):
    """Lists all states with a name starting with N"""
    argUser = argv[1]
    argPswd = argv[2]
    argDbName = argv[3]

    dbConnection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argUser,
        passwd=argPswd,
        db=argDbName
    )
    selectQuery = 'SELECT * FROM states WHERE name LIKE "N%" ORDER BY id'
    cursorDb = dbConnection.cursor()
    cursorDb.execute(selectQuery)
    for row in cursorDb.fetchall():
        print(row)
    cursorDb.close()
    dbConnection.close()


if __name__ == '__main__':
    filterStates()
