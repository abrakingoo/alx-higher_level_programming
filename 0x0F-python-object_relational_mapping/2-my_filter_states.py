#!/usr/bin/python3
"""
 a script that takes in an argument and displays all values in
 the states table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":

    try:
        import MySQLdb
        from sys import argv

        usr, pswd, db, value = argv[1:5]

        conn = MySQLdb.connect(host="localhost", port=3306, user=usr,
                               password=pswd, database=db)

        cur = conn.cursor()

        query = """SELECT *
                    FROM states
                    WHERE BINARY name
                    LIKE '%{}%'
                    ORDER BY
                    states.id""".format(value)

        cur.execute(query)
        states = cur.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("ERROR: {} ".format(e))

    finally:
        cur.close()
        conn.close()
