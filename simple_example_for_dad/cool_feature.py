import datetime
import time
import pyodbc
import pdb
import json

def print_me():
    with open('/tmp/log/out.txt', 'a') as f:
        for i in range(0, 5):
            statement = 'current time: {}\n'.format(datetime.datetime.now())
            print statement
            f.write(statement)
            time.sleep(1)


def write_to_db():
    client = pyodbc.connect('DSN=postgres')
    client.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
    client.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')

    cursor = client.cursor()

    # write bogus rows to a table
    for i in range(0, 5):
        cursor.execute("insert into example_table ( content_string ) values ( 'example string' ) ;")
        cursor.execute("commit;")
        time.sleep(1)

    # fetch back the rows from the table
    cursor.execute('select * from example_table;')
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    print results

if __name__ == '__main__':
    write_to_db()
    print_me()

