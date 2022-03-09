#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    # required arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    name = argv[4]

    # connecting to the database using 'connect()' method
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        database=database_name
    )

    # creating an instance of 'cursor' class which is used to execute
    # the 'SQL' statements in Python
    cursor = db.cursor()

    # getting all the states which are present in database
    # 'execute()' method is used to compile a 'SQL' statement
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
    ORDER BY id ASC".format(name))

    # it returns list of states present in the database
    all_states = cursor.fetchall()

    # showing all the states one by one
    for state in all_states:
        print(state)
    cursor.close()
    db.close()
