#Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести 
# имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных. На Отлично в одного человека 
# надо сделать консольное приложение Телефонный справочник с внешним хранилищем информации, и чтоб был реализован 
# основной функционал - просмотр, сохранение, импорт, поиск, удаление.
   
import os
import sqlite3 as sq

os.system('CLS')

with sq.connect('phone.db') as con:
    cur=con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS phones (
    surname TEXT,
    name TEXT,
    patronymic TEXT,
    phone_number INTEGER
            )""")

def find_number():
    print('Пожалуйста, определите параметр, по которому будет производится поиск:')
    print('1-Фамилия\n2-Имя\n3-Отчество\n4-Номер телефона\n')
    user_choice1=input('Введите номер параметра: ')
    user_choice2=input('Введите значение параметра: ')
    print()
    if user_choice1 == '1':
        sql="""SELECT * FROM phones WHERE surname = ?"""
        cur.execute(sql, (user_choice2,))
        result=cur.fetchall()
        if result==True:
            print(result)
        else:
            print('Нет такого человека')
        print()
    elif user_choice1 == '2':
        sql="""SELECT * FROM phones WHERE name = ?"""
        cur.execute(sql, (user_choice2,))
        result=cur.fetchall()
        if result==True:
            print(result)
        else:
            print('Нет такого человека')
        print()
    elif user_choice1 == '3':
        sql="""SELECT * FROM phones WHERE patronymic = ?"""
        cur.execute(sql, (user_choice2,))
        result=cur.fetchall()
        if result==True:
            print(result)
        else:
            print('Нет такого человека')
        print()
    elif user_choice1 == '4':
        sql="""SELECT * FROM phones WHERE phone_number = ?"""
        cur.execute(sql, (user_choice2,))
        result=cur.fetchall()
        if result==True:
            print(result)
        else:
            print('Нет такого телефона')
        print()

def add_phone_number():
    user_choice1=input('Введите Фамилию контакта: ')
    user_choice2=input('Введите Имя контакта: ')
    user_choice3=input('Введите Отчество контакта: ')
    user_choice4=input('Введите номер телефона контакта: ')
    sql="""INSERT INTO phones VALUES (?, ?, ?, ?)"""
    abc=(user_choice1, user_choice2, user_choice3, user_choice4)
    cur.execute(sql, abc)
    con.commit()

def change_contact():
    user_choice1=input('Введите Фамилию контакта, данные которого Вы хотите изменить: ')
    user_choice2=input('Введите имя: ')
    user_choice3=input('Введите отчество: ')
    user_choice4=input('Введите номер телефона: ')
    sql="""UPDATE phones SET name=?, patronymic=?, phone_number=? WHERE surname=?"""
    values=(user_choice2, user_choice3, user_choice4, user_choice1)
    cur.execute(sql, values)
    con.commit()

def delete_contact ():
    user_choice1=input('Введите Фамилию контакта, данные которого Вы хотите удалить: ')
    sql='DELETE FROM phones WHERE surname=?'
    cur.execute(sql, user_choice1)
    con.commit()

def delete_all_contacts ():
    cur.execute('DELETE FROM phones')
    con.commit()

def show_phonebook():
    cur.execute('SELECT * FROM phones')
    for result in cur:
        print(result)
    print()

while True:
    print('Что Вы хотите сделать?')
    print('1-Найти контакт\n2-Добавить контакт\n3-Изменить контакт\n4-Удалить контакт\n5-Удалить все контакты\n\
6-Просмотреть все контакты\n0-Выход из приложения\n')
    user_choice=input('Введите номер действия: ')
    print()
    if user_choice == '1':
        find_number()
    elif user_choice == '2':
        add_phone_number()
    elif user_choice == '3':
        change_contact()
    elif user_choice == '4':
        delete_contact()
    elif user_choice == '5':
        delete_all_contacts()
    elif user_choice == '6':
        show_phonebook()
    elif user_choice == '0':
        print('До свидания!')
        os.system('CLS')
        break
    else:
        os.system('CLS')
        print('Неправильно выбрана команда!')
        print()
        continue