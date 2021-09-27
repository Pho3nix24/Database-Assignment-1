import sqlite3
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def connect_db(name):
    con = sqlite3.connect(name)
    return con


def insert_values(cur):
    cur.executemany('INSERT INTO Hospital VALUES (?,?,?)',
                    [(1, 'Mayo Clinic', 200), (2, 'Cleveland Clinic', 400), (3, 'Johns Hopkins', 1000),
                     (4, 'UCLA Medical Center', 1500)])
    connection.commit()
    cursor1.executemany('INSERT INTO Doctor VALUES (?,?,?,?,?,?,?)',
                        [(101, 'David', 1, '2005-02-10', 'Pediatric', 40000, 'NULL'),
                         (102, 'Michael', 1, '2018-07-23', 'Oncologist', 20000, 'NULL'),
                         (103, 'Susan', 2, '2016-05-19', 'Gynecologist', 25000, 'NULL'),
                         (104, 'Robert', 2, '2017-12-28', 'Pediatric', 28000, 'NULL'),
                         (105, 'Linda', 3, '2004-06-04', 'Gynecologist', 42000, 'NULL'),
                         (106, 'William', 3, '2012-09-11', 'Dermatologist', 30000, 'NULL'),
                         (107, 'Richard', 4, '2014-08-21', 'Gynecologist', 32000, 'NULL'),
                         (108, 'Karen', 4, '2011-10-17', 'Radiologist', 30000, 'NULL')])
    connection.commit()


def create_tables(cur):
    try:
        cur.execute(
            "CREATE TABLE Hospital (Hospital_ID INTEGER PRIMARY KEY , Hospital_Name VARCHAR(50), Bed_Count INTEGER)")
        cur.execute(
            "CREATE TABLE Doctor (Doctor_ID INTEGER PRIMARY KEY, Doctor_Name VARCHAR(30), Hospital_ID INTEGER, Joining_Date DATE, Speciality VARCHAR(20), Salary INTEGER, Experience INTEGER, FOREIGN KEY (Hospital_ID) references Hospital(Hospital_ID))")
        connection.commit()
        insert_values(cur)
    except sqlite3.OperationalError:
        print("The Table has already been created!!!")


def display_table(table_name):
    print("{} Table\n******************************************************************************************".format(
        table_name))
    print(pd.read_sql_query("SELECT * FROM {}".format(table_name), connection))
    print("******************************************************************************************")


if __name__ == "__main__":
    hospital_id = 0
    hospital_id_list = []
    connection = connect_db('HospitalDB.db')
    cursor1 = connection.cursor()
    create_tables(cursor1)
    display_table('Hospital')
    display_table('Doctor')
    connection.commit()
    while True:
        try:
            speciality = input("Enter the speciality : ")
            salary = input("Enter the salary : ")
            query1 = "SELECT * FROM Doctor WHERE Speciality='{}' and Salary>={}".format(speciality.capitalize(), salary)
            print("******************************************************************************************")
            print(pd.read_sql_query(query1, connection))
            print("******************************************************************************************")
        except ValueError:
            print("Invalid Value")
        except pd.io.sql.DatabaseError:
            print("Invalid Query!!!")
        else:
            break
    while True:
        try:
            hospital_id = int(input("Enter Hospital ID : "))
        except ValueError:
            print("Invalid Value!!!")
            continue
        cursor1.execute("SELECT DISTINCT(Hospital_ID) FROM Doctor")
        temp_list = cursor1.fetchall()
        for item in temp_list:
            hospital_id_list.append(int(item[0]))
        if hospital_id not in hospital_id_list:
            print("Hospital Does not Exist!!!!")
        else:
            break
    query2 = "SELECT Doctor_Name,Hospital_Name FROM Hospital,Doctor WHERE Hospital.Hospital_ID=Doctor.Hospital_ID and Hospital.Hospital_ID={}".format(
        hospital_id)
    print(
        "List of Doctors along with their Hospital Name\n******************************************************************************************")
    print(pd.read_sql_query(query2, connection))
    print("******************************************************************************************")
