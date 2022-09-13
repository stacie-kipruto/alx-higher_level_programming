#!/usr/bin/python3
"""
2-my_filter_states: select statess matching argument
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
    cur.execute("SELECT * FROM states WHERE name LIKE \
        '{}' ORDER BY id".format(sys.argv[4]))
    results = cur.fetchall()
    for result in results:
        print(result)
    cur.close()
