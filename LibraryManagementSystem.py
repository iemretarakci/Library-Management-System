import sqlite3
import tkinter as tk

DB = sqlite3.connect("database.db")
cursor = DB.cursor()
#Book Add Function
def Add():
    name_add = entry_name_add.get()
    author_add= entry_author_add.get()
    cursor.execute("INSERT INTO Books(name,author) VALUES(?,?)", (name_add, author_add))
    DB.commit()
#Book Search Function
def Search():
    name_search = entry_name_search.get()
    author_search = entry_author_search.get()
    if not name_search and author_search:
        cursor.execute("SELECT * FROM Books WHERE author=? ", (author_search))
        rows=cursor.fetchall()
        for row in rows:
            print(row)    
    elif name_search and not author_search:
        cursor.execute("SELECT * FROM Books WHERE name=?", (name_search))
        rows=cursor.fetchall()
        for row in rows:
            print(row) 
    elif name_search and author_search:
        cursor.execute("SELECT * FROM Books WHERE name=? AND author=?", (name_search, author_search))
        rows=cursor.fetchall()
        for row in rows:
            print(row)
    else:
        cursor.execute("SELECT * FROM Books")
        rows= cursor.fetchall()
        for row in rows:
            print(row)      
                        
#Application Window Features
App = tk.Tk()
App.title("Library Management System")
App.geometry("700x400")

#Adding Books 
lbl_add=tk.Label(App,text="Register Book",font="Times 12")
lbl_add.place(x=1,y=1)
entry_name_add = tk.Entry(App,textvariable=str,width=25)
entry_name_add.place(x=10,y=30)
entry_author_add = tk.Entry(App,textvariable=str,width=25)
entry_author_add.place(x=10,y=50)
button_register_add = tk.Button(App, text="Add",padx=20,pady=5,command=Add)
button_register_add.place(x=10,y=70)

#Searching Books
lbl_search=tk.Label(App,text="Search Book",font="Times 12")
lbl_search.place(x=300,y=1)
entry_name_search = tk.Entry(App,textvariable=str,width=25)
entry_name_search.place(x=300,y=30)
entry_author_search = tk.Entry(App,textvariable=str,width=25)
entry_author_search.place(x=300,y=50)
button_search = tk.Button(App,text="Search",padx=20,pady=5,command=Search)
button_search.place(x=300,y=70)

#Removing Books

App.mainloop()