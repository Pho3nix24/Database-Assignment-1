import sqlite3
import pandas as pd


def connect_db(name):
    con = sqlite3.connect(name)
    return con


def create_table_cars(cur):
    try:
        cur.execute("CREATE TABLE Cars (Name_of_Car varchar(20), Name_Of_Owner varchar(20))")
        connection.commit()
    except sqlite3.OperationalError:
        print("The Table has already been created!!!")


def insert_values(cur, val1, val2):
    insert_query = "INSERT INTO Cars(Name_of_Car,Name_of_Owner) VALUES (?,?)"
    cur.execute(insert_query, (val1, val2))
    connection.commit()


if __name__ == "__main__":
    number_of_inputs = 0
    connection = connect_db('CarsDB.db')
    cursor1 = connection.cursor()
    create_table_cars(cursor1)
    while True:
        try:
            number_of_inputs = int(input("Enter the number of records to be inserted : "))
        except ValueError:
            print("Invalid Value!!!")
        else:
            break
    for index in range(number_of_inputs):
        car = input("Enter name of car : ")
        owner = input("Enter name of owner : ")
        insert_values(cursor1,car,owner)
    print("Cars Table\n************************************************")
    print(pd.read_sql_query("SELECT * FROM Cars", connection))
    print("************************************************")


