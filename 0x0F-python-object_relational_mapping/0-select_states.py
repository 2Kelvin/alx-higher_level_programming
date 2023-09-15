#!/usr/bin/python3
"""Get all states script"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    myDatabase = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

myCursor = myDatabase.cursor()
myQuery = 'SELECT * FROM states ORDER BY states.id'
myCursor.execute(myQuery)
allRows = myCursor.fetchall()

for oneRow in allRows:
    print(oneRow)

myCursor.close()
myDatabase.close()
