from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import mysql.connector as mysql

##########################################################################################################################################################################

# file handling
#logging process

def log(lines):
    in_file = "entry_result.txt"
    file = open(in_file,'a+')
    
    file.write(f"{lines}\n\n")

##########################################################################################################################################################################

# mysql connection

try :
    connection = mysql.connect(user="root",password="2684",host="localhost",database="htlmgmt",port=3306)
except mysql.errors.ProgrammingError as e:
    log("No database found, Creating one...")
    atrcon = mysql.connect(user="root",password="2684",host="localhost",port=3306)
    c = atrcon.cursor()
    qry = "create database htlmgmt;"
    c.execute(qry)
    atrcon.commit()
    log("Creating Database...")

try :
    cursor = connection.cursor()
except NameError as e:
    connection = mysql.connect(user="root",password="2684",host="localhost",database="htlmgmt",port=3306)
    
cursor = connection.cursor()
print("Connection success can proceed without any problem's")

##########################################################################################################################################################################
    
# creating mysql entry function

def check_in(Id,Name,Date,Time,Number):
    query = f'insert into check_in value("{Id}","{Name}","{Date}","{Time}","{Number}");'
    
    # error handling  
    try :
        cursor.execute(query)  
    except mysql.errors.ProgrammingError as e:
        log("No table found,creating one...")
        atr = f"create table check_in(ID char(50),Name char(50),Date char(50),Time char(50),Number char(50));"
        cursor.execute(atr)
        connection.commit()
        log("Successfully created table check_in")
    cursor.execute(query)
    connection.commit()
    data = cursor.statement
    log(data)
    mb.showinfo("Successfull","Checked in successfully")

def check_out(Id,Name,Date,Time,Amount):
    query = f'insert into check_out value("{Id}","{Name}","{Date}","{Time}","{Amount}");'

    # error handling  
    try :
        cursor.execute(query)
    except mysql.errors.ProgrammingError as e:
        log("No table found, creating one..")
        atr = f"create table check_out(ID char(50),Name char(50),Date char(50),Time char(50),Amount char(50));"
        cursor.execute(atr)
        connection.commit()
        log("Successfully created table check_out")

    cursor.execute(query)
    connection.commit()
    data = cursor.statement
    log(data)
    mb.showinfo("Successfull","Checked out successfully")    

##########################################################################################################################################################################

# global button functions

def in_Vals():
    in_win = Tk()
    in_win.title("Check In Details")
    in_win.geometry("700x700")
    in_win.resizable(0,0)

    # title

    title = Label(in_win,text="Check In Details",font=("Harlow Solid Italic",30,"italic"),fg="black",bg="#fbb08c")
    title.pack(anchor="center",pady=5)

    #creating label's
    _Id_ = Label(in_win,text="Room ID :",font=("Times New Roman",15,"italic"),fg="black",bg="#fbb08c")
    _Name_ = Label(in_win,text="Name :",font=("Times New Roman",15,"italic"),fg="black",bg="#fbb08c")
    _Date_ = Label(in_win,text="Date :",font=("Times New Roman",15,"italic"),fg="black",bg="#fbb08c")
    _Time_ = Label(in_win,text="Time :",font=("Times New Roman",15,"italic"),fg="black",bg="#fbb08c")
    _Number_ = Label(in_win,text="Number :",font=("Times New Roman",15,"italic"),fg="black",bg="#fbb08c")
    
    
    _Id_.pack(anchor='w',padx=10,pady=20)
    _Name_.pack(anchor='w',padx=10,pady=20)
    _Date_.pack(anchor='w',padx=10,pady=20)
    _Time_.pack(anchor='w',padx=10,pady=20)
    _Number_.pack(anchor='w',padx=10,pady=20)

    
    # creating submit function

    def submit():
        in_val_1 = Id.get()
        in_val_2 = Name.get()
        in_val_3 = Date.get()
        in_val_4 = Time.get()
        in_val_5 = Number.get()
        result = check_in(in_val_1,in_val_2,in_val_3,in_val_4,in_val_5)


    # creating entries

    Id = Entry(in_win,width=25,font=("Courier",15,'bold'))
    Name = Entry(in_win,width=25,font=("Courier",15,'bold'))
    Date = Entry(in_win,width=25,font=("Courier",15,'bold'))
    Time = Entry(in_win,width=25,font=("Courier",15,'bold'))
    Number = Entry(in_win,width=25,font=("Courier",15,'bold'))

    Id.place(x=100,y=87)
    Name.place(x=100,y=157)
    Date.place(x=100,y=227)
    Time.place(x=100,y=293)
    Number.place(x=100,y=360)
    
    # creating submit button

    submit = Button(in_win,text="Submit",font=("Wild Latin",15,"bold"),command=submit)
    submit.place(x = 250,y=450)
    
    in_win.config(bg="#fbb08c")
    in_win.mainloop()

    ################################################################################################################################################################

def out_Vals():
    out_win = Tk()
    out_win.title("Check In Details")
    out_win.geometry("700x700")
    out_win.resizable(0,0)

    # title

    title = Label(out_win,text="Check Out Details",font=("Harlow Solid Italic",30,"italic"),fg="black",bg="#fbb08c")
    title.pack(anchor="center",pady=5)

    #creating label's
    _Id_ = Label(out_win,text="Room ID :",font=("Times New Roman",15,"italic"),fg="black",bg="#fbb08c")
    _Name_ = Label(out_win,text="Name :",font=("Times New Roman",15,"italic"),fg="black",bg="#fbb08c")
    _Date_ = Label(out_win,text="Date :",font=("Times New Roman",15,"italic"),fg="black",bg="#fbb08c")
    _Time_ = Label(out_win,text="Time :",font=("Times New Roman",15,"italic"),fg="black",bg="#fbb08c")
    _Amount_ = Label(out_win,text="Amount :",font=("Times New Roman",15,"italic"),fg="black",bg="#fbb08c")
    
    
    _Id_.pack(anchor='w',padx=10,pady=20)
    _Name_.pack(anchor='w',padx=10,pady=20)
    _Date_.pack(anchor='w',padx=10,pady=20)
    _Time_.pack(anchor='w',padx=10,pady=20)
    _Amount_.pack(anchor='w',padx=10,pady=20)

    
    # creating submit function

    def submit():
        out_val_1 = Id.get()
        out_val_2 = Name.get()
        out_val_3 = Date.get()
        out_val_4 = Time.get()
        out_val_5 = Amount.get()
        result = check_out(out_val_1,out_val_2,out_val_3,out_val_4,out_val_5)

    # creating entries

    Id = Entry(out_win,width=25,font=("Courier",15,'bold'))
    Name = Entry(out_win,width=25,font=("Courier",15,'bold'))
    Date = Entry(out_win,width=25,font=("Courier",15,'bold'))
    Time = Entry(out_win,width=25,font=("Courier",15,'bold'))
    Amount = Entry(out_win,width=25,font=("Courier",15,'bold'))

    Id.place(x=100,y=87)
    Name.place(x=100,y=157)
    Date.place(x=100,y=227)
    Time.place(x=100,y=293)
    Amount.place(x=100,y=360)
    
    # creating submit button

    submit = Button(out_win,text="Submit",font=("Wild Latin",15,"bold"),command=submit)
    submit.place(x = 250,y=450)
    
    out_win.config(bg="#fbb08c")
    out_win.mainloop()


##########################################################################################################################################################################

def main_win():
    scr = Tk()
    scr.title("Hotel Management")
    scr.config(bg="#bbecb3")
    scr.geometry("700x700")
    scr.resizable(0,0)

    # adding Label

    Title = Label(scr,text="Hotel Reservation Management",font=("Harlow Solid Italic",35,"italic"),bg="#bbecb3",fg="red")
    Title.pack(anchor="center",pady=5)
    
    # adding button's to the following screen 
    
    In = Button(scr,text="CHECK-IN",font=("Times New Roman",15,"bold"),fg="black",bg="#7b61e4",width=20,command=in_Vals)
    In.pack(padx=5,pady=100,ipadx=2,ipady=2,anchor="w")
    
    Out = Button(scr,text="CHECK-OUT",font=("Times New Roman",15,"bold"),fg="black",bg="#7b61e4",width=20,command=out_Vals)
    Out.pack(padx=5,pady=1,ipadx=2,ipady=2,anchor="w")
    
    
    
    scr.mainloop()

##########################################################################################################################################################################
main_win()
