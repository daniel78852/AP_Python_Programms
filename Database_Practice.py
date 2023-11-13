import os.path
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import openpyxl
from openpyxl.styles import *
import  sqlite3

#Variables

#Functions

def enter_data():
    terms_cond_checked = term_check_var.get()
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()

    if terms_cond_checked == "Accepted" and firstname and lastname:


        title = titl_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()
        registered_status = registered_check_var.get()
        num_courses = num_courses_spinbox.get()
        num_semesters = num_semesters_spinbox.get()


        print (f'Dear {title} {lastname}, {firstname}, \n' \
               f'age: {age}\n' 
               f'nationality: {nationality}\n'
               f'{registered_status}\n'
               f'Number of courses taken: {num_courses}\n'
               f'Is currently in Semester {num_semesters}\n'
               f'{terms_cond_checked}.')

            #Using openpyxl

#        filepath = "D:\PythonClass\data.xlsx"
#        if not os.path.exists(filepath):
#            workbook = openpyxl.Workbook()
#            sheet = workbook.active
#            heading = ["Title","First Name", "Last Name", "Age", "Nationality",
#                       "# Courses", "# Sessions", "Registered Status"]
#            sheet.append(heading)
#            workbook.save(filepath)

#        workbook = openpyxl.load_workbook(filepath)
#        sheet = workbook.active
#       sheet.append([title, firstname, lastname, age, nationality,
#                      registered_status, num_courses, num_semesters,
#                      terms_cond_checked])





#       workbook.save(filepath)

#    else:
#        tkinter.messagebox.showwarning(
#            title="Terms & Conditions",
#            message="Please fill in your first and last name and check the 'Terms & Conditions'")

            #Using SQLite3
        #Connect to Sqlite3 table
        conn = sqlite3.connect("StudentDataBase.db")

        table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data
        (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT,
        registered_status TEXT, num_courses INT, num_semesters INT)
        '''
        conn.execute(table_create_query)

        data_insert_query = '''INSERT INTO Student_Data(firstname, lastname,
                                   title, age, nationality,registered_status, 
                                   num_courses, num_semesters) 
                                   VALUES(?,?,?,?,?,?,?,?)
                                   '''
        data_insert_tuple = (firstname, lastname,title,
                             age,nationality, registered_status,
                             num_courses, num_semesters)

        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()


        #Close table
        conn.close()


def exit():
    print("App exited")
    window.destroy()


#Mainloop

window = tkinter.Tk()
window.title("Data Entry Form")

frame = Frame(window, highlightbackground="red", highlightthickness=2 )
frame.pack()

#Saving user information
user_info_frame = LabelFrame(frame, text="User Information", )
user_info_frame.grid(row=0,column=0, padx=20, pady=20 )

first_name_label = Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column= 0)

last_name_label = Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column= 1)

first_name_entry = Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_entry = Entry(user_info_frame)
last_name_entry.grid(row= 1, column=1)

title_label = Label(user_info_frame, text="Title")
title_label.grid(row=0, column=2)

titl_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Mrs.","Ms.","Dr.", "None"])
titl_combobox.grid(row=1, column=2)


age_label = Label(user_info_frame, text= "Age")
age_label.grid(row=2, column=0)

age_spinbox = Spinbox(user_info_frame, from_=18,to=110)
age_spinbox.grid(row=3, column=0)

nationality_label= Label(user_info_frame, text="Nationality")
nationality_label.grid(row= 2,column=1)

nationality_combobox = ttk.Combobox(user_info_frame, values=["American", "Mexican","South Korean", "Japanese"])
nationality_combobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Part 2 2md label Frame

courses_Frame = LabelFrame(frame,text= "Course Information", )
courses_Frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

registered_label = Label(courses_Frame, text="Registration Status")
registered_label.grid(row=0, column=0)


registered_check_var = tkinter.StringVar(value="Not Registered")
registered_check = Checkbutton(courses_Frame, text="Currently Registered",
                               variable=registered_check_var,
                               onvalue="Registered",
                               offvalue="Not Registered")
registered_check.grid(row=1, column=0)

num_courses_label = Label(courses_Frame, text="No. Courses")
num_courses_label.grid(row=0, column=1)

num_courses_spinbox = Spinbox(courses_Frame, from_=0,to=8)
num_courses_spinbox.grid(row=1,column=1)


num_semesters_label = Label(courses_Frame, text="# Semesters")
num_semesters_label.grid(row=0,column=2)

num_semesters_spinbox = Spinbox(courses_Frame, from_=1,to=4)
num_semesters_spinbox.grid(row=1, column=2)


for widgets in courses_Frame.winfo_children():
    widgets.grid_configure(padx=10, pady=5)


#Label Frame 3

terms_frame = LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=20)

term_check_var = tkinter.StringVar(value="Not Accepted")
term_check = Checkbutton(terms_frame,text="I accept the terms and conditions.",
                         variable=term_check_var,
                         onvalue="Accepted",
                         offvalue="Not Accepted")
term_check.grid(row=0, column=0)


#Buttons
enter_button = ttk.Button(frame, text="Enter", command=enter_data)
enter_button.grid(row=3, column=3)

exit_button = ttk.Button(frame, text="Exit", command=exit)
exit_button.grid(row=4, column=3)

for widgets in frame.winfo_children():
    widgets.grid_configure(padx=10, pady= 5)



#Mainloop
window.mainloop()