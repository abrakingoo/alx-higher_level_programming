#!/usr/bin/python3
"""
 a script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":

    try:
        from sys import argv
        import MySQLdb

        usr, pwd, db = argv[1:4]

        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=usr, password=pwd, database=db)

        cur = conn.cursor()

        query = "SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id ORDER BY cities.id"
        cur.execute(query)

        cities = cur.fetchall()

        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print(e)

    finally:
        cur.close()
        conn.close()
