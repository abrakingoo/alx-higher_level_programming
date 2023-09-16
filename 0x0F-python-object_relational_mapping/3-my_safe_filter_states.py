#!/usr/bin/python3
"""
 a script that takes in arguments and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument. But this time,
 it is safe from MySQL injections!
"""

if __name__ == "__main__":

    try:
        import MySQLdb
        from sys import argv

        usr, pwd, db, data = argv[1:5]

        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=usr, password=pwd, database=db)

        cur = conn.cursor()

        query = "SELECT * FROM states WHERE BINARY name = %s"

        cur.execute(query, (data,))

        states = cur.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"ERROR: {e}")

    finally:
        cur.close()
        conn.close()
