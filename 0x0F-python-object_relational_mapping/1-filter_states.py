#!/usr/bin/python3
"""
a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    try:
        conn = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            port=3306,
            db=argv[3]
        )

        query = """
        SELECT *
        FROM states
        WHERE BINARY name LIKE 'N%'
        ORDER BY id ASC
        """
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("execution failed")
    cur.close()
    conn.close()
