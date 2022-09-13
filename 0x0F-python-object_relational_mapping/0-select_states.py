#!/usr/bin/python3
"""
0-select_states: lists all states in database table
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
      host="localhost",
      user=sys.argv[1],
      passwd=sys.argv[2],
      database=sys.argv[3],
      port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    results = cur.fetchall()
    for result in results:
        print(result)
    cur.close()
