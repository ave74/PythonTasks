#Задача: 
# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.
   
import os
import sqlite3 as sq
import datetime

os.system('CLS')

with sq.connect('Notes.db') as con:
    cur=con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS notes (
    noteID INTEGER PRIMARY KEY,
    date timestamp,
    header TEXT NOT NULL,
    note TEXT
            )""")

def find_note():
    print('Пожалуйста, определите параметр, по которому будет производится поиск:')
    print('1-ID заметки\n2-Дата\n3-Заголовок\n4-Ключевое слово в заметке\n')
    user_choice1=input('Введите номер параметра: ')
    user_choice2=input('Введите значение параметра: ')
    print()
    if user_choice1 == '1':
        sql="""SELECT * FROM notes WHERE noteID = ?"""
        cur.execute(sql, user_choice2)
        result=cur.fetchall()
        if result==[]:
            print('Нет такой заметки')
        else:
            print(*result)
        print()
    elif user_choice1 == '2':
        sql="""SELECT * FROM notes WHERE date LIKE ('%' || ? || '%')"""
        cur.execute(sql, (user_choice2,))
        result=cur.fetchall()
        if result==[]:
            print('Нет такой заметки')
        else:
            print(*result)
        print()
    elif user_choice1 == '3':
        sql="""SELECT * FROM notes WHERE header LIKE ('%' || ? || '%')"""
        cur.execute(sql, (user_choice2,))
        result=cur.fetchall()
        if result==[]:
            print('Нет такой заметки')
        else:
            print(*result)
        print()
    elif user_choice1 == '4':
        sql="""SELECT * FROM notes WHERE note LIKE ('%' || ? || '%')"""
        cur.execute(sql, (user_choice2,))
        result=cur.fetchall()
        if result==[]:
            print('Нет такой заметки')
        else:
            print(*result)
        print()

def add_note():
    user_choice3=input('Введите заголовок заметки: ')
    user_choice4=input('Введите заметку: ')
    sql="""INSERT INTO notes VALUES (?, ?, ?, ?)"""
    cur.execute('SELECT max(noteID) FROM notes')
    row=cur.fetchone()[0]
    if row==None:
        rowID=1
    else:
        rowID=row+1
    values=(rowID, datetime.datetime.now(), user_choice3, user_choice4)
    cur.execute(sql, values)
    con.commit()

def change_note():
    user_choice1=input('Введите номер заметки, которую Вы хотите изменить: ')
    user_choice3=input('Введите заголовок заметки: ')
    user_choice4=input('Введите заметку: ')
    sql="""UPDATE notes SET date=?, header=?, note=? WHERE noteID=?"""
    values=(datetime.datetime.now(), user_choice3, user_choice4, user_choice1)
    cur.execute(sql, values)
    con.commit()

def delete_note ():
    user_choice1=input('Введите номер заметки, которую Вы хотите удалить: ')
    sql='DELETE FROM notes WHERE noteID=?'
    cur.execute(sql, user_choice1)
    con.commit()

def delete_all_notes ():
    cur.execute('DELETE FROM notes')
    con.commit()

def show_notes():
    cur.execute('SELECT * FROM notes')
    for result in cur:
        print(result)
    print()

while True:
    print('Что Вы хотите сделать?')
    print('1-Найти заметку\n2-Добавить заметку\n3-Изменить заметку\n4-Удалить заметку\n5-Удалить все заметки\n\
6-Просмотреть все заметки\n0-Выход из приложения\n')
    user_choice=input('Введите номер действия: ')
    print()
    if user_choice == '1':
        find_note()
    elif user_choice == '2':
        add_note()
    elif user_choice == '3':
        change_note()
    elif user_choice == '4':
        delete_note()
    elif user_choice == '5':
        delete_all_notes()
    elif user_choice == '6':
        show_notes()
    elif user_choice == '0':
        print('До свидания!')
        os.system('CLS')
        break
    else:
        os.system('CLS')
        print('Неправильно выбрана команда!')
        print()
        continue