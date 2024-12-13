import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'lataharish28',
        database = 'student_management'
    )

    if connection.is_connected():
        print("Connection Establisted Successfully...")

except Error as e:
    print("Failed to establish connection",e)
    exit()


def create_student():

    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    roll_number = input("Enter Roll No.: ")
    section = input("Enter Section: ")
    attendence = input("Enter Attendence: ")

    try:
        cursor = connection.cursor()
        query = "INSERT INTO student (name,branch,roll_number,section,attendence) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query,(name,branch,roll_number,section,attendence))
        connection.commit()
        print("Student is inserted successfully...")
    
    except Error as e:
        print("Failed to insert student",e)
    
def view_student():

    try:
        cursor = connection.cursor()
        query = "SELECT * FROM student"
        cursor.execute(query)
        data = cursor.fetchall()
        print("Student Data")
        print("ID\tNAME\tBRANCH\tROLL No.\tSECTION\tATTENDENCE")
        
        for each in data:
            print(f"{each[0]}\t{each[1]}\t{each[2]}\t{each[3]}\t{each[4]}\t{each[5]}\t")
        
    except Error as e:
        print("Failed to fetch data",e)

def update_student():
    student_id = input("Enter Student ID to update: ")
    column = input("Enter the field to update (name/branch/roll_number/section/attendence): ")
    new_value = input(f"Enter the new value for {column}: ")

    try:
        cursor = connection.cursor()
        query = f"UPDATE student SET {column} = %s WHERE id = %s"
        cursor.execute(query,(new_value,student_id))
        connection.commit()
        print("Student is updated successfully...")

    except Error as e:
        print("Failed to update student",e)

def delete_student():
    student_id = input("Enter the STUDENT ID to delete: ")

    try:
        cursor = connection.cursor()
        query = "DELETE FROM student WHERE id = %s"
        cursor.execute(query,(student_id,))
        connection.commit()
        print("Student is deleted successfully")
    
    except Error as e:
        print("Failed to delete student",e)

print(" *-----* Welcome to Student Management System *-----* ")
print("------------------------------------------------------")
while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter Your Choice: ")
    print("----------------------------")


    if choice == '1':
        create_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting from the system")
        break
        
    else: 
        print("Invalid Choice,please try again!!")




if connection.is_connected():
    connection.close()
    print("Connection closed...")