#!/usr/bin/python3
"""
a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    user = argv[1]
    pswrd = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=user, password=pswrd, database=db)

    cur = conn.cursor()
    querry = f"SELECT * FROM states WHERE name \
                LIKE 'N%' ORDER BY states.id ASC"
    cur.execute(querry)
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
