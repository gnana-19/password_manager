import sqlite3
from random import *
import random

connection = sqlite3.connect("passwords.db")
crsr = connection.cursor()


def Query(site):
    q = "select password from passwords where site_name ='" + site + "'"
    return q

def insert_query(obj):
    Q = "insert into passwords values ('" + obj.site_name + "','" + obj.password + "')"
    return Q


class password_class:
    site_name = None
    password = None
    def __init__(self,site,password):
        self.site_name = site
        self.password = password
    def __repr__(self):
        return self.site_name + " " + self.password
    
def retrive_password(site):
    query = Query(site)
    crsr.execute(query)
    ans = crsr.fetchall()
    # crsr.close()
    return ans

def get_new_password():
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@#$%&*+"
    strings = [caps,low,digits,special]
    length = randint(8,16)
    password = ""
    ind = randint(0,25)
    password += caps[ind]
    ind = randint(0,25)
    password += low[ind]
    ind = randint(0,9)
    password += digits[ind]
    ind = randint(0,7)
    password += special[ind]
    length -= 4
    for i in range(length):
        ind = randint(0,3)
        str_len = len(strings[ind])
        ind2 = randint(0,str_len-1)
        password += strings[ind][ind2]
    ''.join(random.sample(password,len(password)))
    return password

def insert(obj):
    print(obj)
    query = insert_query(obj)
    crsr.execute(query)
    connection.commit()
    # print(query)

def new_password():
    print("Enter site")
    site = input()
    password = get_new_password()
    print(password)
    print("do you want to insert into table ?")
    responce = input()
    if responce == "NO" or responce == "no" or responce == "No":
        print("Thank-you")
    else:
        obj = password_class(site,password)
        insert(obj)
    
    

def old_password():
    print("Enter site")
    site = input()
    password = retrive_password(site)
    try:
        print(password[0])
    except IndexError: 
        print("no site found")

def print_table():
    crsr.execute("select * from passwords")
    for x in crsr.fetchall():
        print(x)
    # crsr.close()


def add_password():
    print("site :-")
    site = input()
    print("password :- ")
    password = input()
    obj = password_class(site,password)
    insert(obj)

def delete_(site_name):
    return "delete from passwords where site_name = '" + site_name + "'"

def delete_row():
    print("enter site name :-")
    site_name = input()
    query = delete_(site_name)
    try:
        crsr.execute(query)
    except :
        print(site_name, "not found!!")
    connection.commit()

if __name__ == "__main__":
    print("Hi Deepak..\nEnter \n1 :- get Old password\n2 :- create new password\n3 :- print full table\n4 :- add password\n5 :- delete a site\n6 :- exit")
    choice = int(input())
    if choice == 1:
        print("GAJINI\nGAJINI")
        old_password()
    elif choice == 2:
        new_password()
    elif choice == 3:
        print_table()
    elif choice == 4:
        add_password()
    elif choice == 5:
        delete_row()
    connection.close()
    
