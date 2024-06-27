# -*- coding: utf8 -*-
import sqlite3 as sl

con = sl.connect('students.db')
cursor = con.cursor()

class University():
    def __init__(self, Name):
        self.Name = Name

    def add_student(self, id, age, name):
        try:
            sqlite_add = """INSERT INTO students VALUES (?, ?, ?);"""
            data = (id, name, age)
            cursor.execute(sqlite_add, data)
            con.commit()
            print("Новый студент успешно добавлен в базу данных!")
            cursor.close()
        except sl.Error as error:
            print("Ошибка при работе с базой данных!")

    def add_grade(self, id, id_student, subject, grade):
        try:
            sqlite_add = """INSERT INTO grades VALUES (?, ?, ?, ?);"""
            data = (id, id_student, subject, grade)
            cursor.execute(sqlite_add, data)
            con.commit()
            print("Оценки студентам успешно выставлены!")
            cursor.close()
        except sl.Error as error:
            print("Ошибка при работе с базой данных!")

    def get_students(self, subject=None):

        sqlite_select = """SELECT * from students"""
        cursor.execute(sqlite_select)
        records = cursor.fetchall()

        for row in records:
            if subject == None:
                sqlite_select1 = """SELECT * from grades where id_students = ?"""
                cursor.execute(sqlite_select1, (row[0],))
                records1 = cursor.fetchall()
                for row1 in records1:
                    print("Name -", row[1], "Age -", row[2], "Subject -", row1[2], "Grade -", row1[3])
            else:
                sqlite_select1 = """SELECT * from grades where id_students = ? and subject = ?"""
                cursor.execute(sqlite_select1, (row[0], subject,))
                records1 = cursor.fetchall()
                for row1 in records1:
                    print("Name -", row[1], "Age -", row[2], "Subject -", row1[2], "Grade -", row1[3])


        cursor.close()





U = University('Urban')
U.get_students()



