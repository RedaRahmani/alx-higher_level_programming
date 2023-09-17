#!/usr/bin/python3
"""states models
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    host_db = "localhost"
    user_db = sys.argv[1]
    password_db = sys.argv[2]
    name_db = sys.argv[3]
    port = 3306
    state_name = sys.argv[4]  # "your_database_name"
    query = "SELECT name FROM cities WHERE state_id = \
(SELECT id FROM states WHERE name LIKE BINARY %s) ORDER BY cities.id ASC"
    params = (state_name,)
    db = MySQLdb.connect(
        host=host_db, user=user_db, passwd=password_db, db=name_db, port=port
    )
    cursor = db.cursor()

    cursor.execute(query, params)
    rows = cursor.fetchall()
    tuples = ()
    for row in rows:
        tuples += row
    print(*tuples, sep=", ")

    cursor.close()
    db.close()

