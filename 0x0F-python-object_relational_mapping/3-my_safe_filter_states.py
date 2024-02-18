#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
but safe from MySQL injections!
"""
import MySQLdb
from sys import argv

# This code should not be executed when imported
if __name__ == '__main__':

    # To make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Gives us the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # To clean up process
    cur.close()
    db.close()
