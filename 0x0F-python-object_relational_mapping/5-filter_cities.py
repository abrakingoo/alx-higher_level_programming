#!/usr/bin/python3
"""
 a script that takes in the name of a state as an argument and lists
 all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":

    try:
        from sys import argv
        import MySQLdb

        usr, pwd, db, value = argv[1:5]

        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=usr, password=pwd, database=db)

        cur = conn.cursor()

        query = """SELECT cities.name FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    WHERE BINARY states.name = %s
                    ORDER BY cities.id
                """

        cur.execute(query, (value, ))

        cities = cur.fetchall()

        print(", ".join([city[0] for city in cities]))

    except MySQLdb.Error:
        print("execution failed")

    cur.close()
    conn.close()
