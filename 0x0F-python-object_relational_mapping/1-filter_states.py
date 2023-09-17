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

    db = MySQLdb.connect(
        host=host_db, user=user_db, passwd=password_db, db=name_db, port=port
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name \
LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
