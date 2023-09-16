#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa:
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    username = argv[1]
    password = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, password=password, database=db)

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
