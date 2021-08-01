# Import Required Library
from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import Calendar
import csv
import os.path

 
#Exception
class ValueWrong(Exception):
    pass

# Create Object
basis = Tk()

# Set geometry
basis.geometry("400x400")
 

# Add Calendar
cal = Calendar(basis, selectmode = 'day')
cal.pack(pady = 20)

#List for header
header = ['Date', 'Time', 'Appointment']

#Function for time
def time_func(h, m):
    time = f'{h:02d}:{m:02d}'
    return time


#Function hour and minutes within Range
def value_check(h ,m):
    return (0 <= h <= 23) and (0 <= m <= 59)


#Error window
def error_number_window(window):
    tkErrorWindow = Toplevel(window)
    tkErrorWindow.title('Error')
    tkErrorWindow.geometry('200x100')
    labelError = Label(master=tkErrorWindow, bg='red', text='Value not a Number \n hour : 0-24 \n min: 0-59')
    labelError.place(x=30, y=10, width=150, height=80)

def error_window(window):
    tkErrorWindow = Toplevel(window)
    tkErrorWindow.title('Error')
    tkErrorWindow.geometry('200x100')
    labelError = Label(master=tkErrorWindow, text='No Calendar File Found!')
    labelError.place(x=30, y=10, width=150, height=80)

def error_NotFound_window():
    tkErrorWindow = Toplevel(basis)
    tkErrorWindow.title('Error')
    tkErrorWindow.geometry('200x100')
    labelError = Label(master=tkErrorWindow, text='No Appointment found!')
    labelError.place(x=30, y=10, width=150, height=80)


#Function for Set Button
def press_set_button(d, h, m, a, x):
    #check if entry values are number between 00:00 and 23:59
    try:
        hour = int(h.get())
        min = int(m.get())
        if not value_check(hour, min):
            raise ValueWrong
    except (ValueError, ValueWrong):
       return error_number_window(x)
    time = time_func(hour, min)
    appTag = a.get()
    appointment = [d, time, appTag]
    #opens csv and writes list 
    if os.path.exists('./dockerfolder/myCal.csv'):
        with open('./dockerfolder/myCal.csv','a', newline= '') as mycal:
            writer = csv.writer(mycal)
            writer.writerow(appointment)  
    else:
        with open('./dockerfolder/myCal.csv','w', newline= '') as mycal:
            writer = csv.writer(mycal)
            writer.writerow(header)
            writer.writerow(appointment)
    # closes window
    x.destroy()
    


#Function for delete Button 
def press_delete_button(d, h, m, a, x):
    #check if entry values are number between 00:00 and 23:59
    try:
        hour = int(h.get())
        min = int(m.get())
        if not value_check(hour, min):
            raise ValueWrong
    except (ValueError, ValueWrong):
       return error_number_window(x)
    time = time_func(hour, min)
    appTag = a.get()
    appointment = [d, time, appTag]
    found = False
    #opens csv and writes list 
    try:
        with open('./dockerfolder/myCal.csv','r', newline= '') as mycal:
            reader = csv.reader(mycal)
            appointments = list(reader)
        with open('./dockerfolder/myCal.csv', 'w', newline= '') as mycal:  
            writer = csv.writer(mycal)
            for y in range(len(appointments)):
                if appointments[y] == appointment:
                    appointments.pop(y)
                    writer.writerows(appointments)
                    found = True
                    break     
    except FileNotFoundError:
        x.destroy()
        return error_window(basis) 
    # checks if appointment was found
    if found:
        x.destroy()
    else:
        with open('./dockerfolder/myCal.csv', 'w', newline= '') as mycal:  
            writer = csv.writer(mycal)
            writer.writerows(appointments)
        error_NotFound_window()
        x.destroy()


    

#Window to set Appointment
def set_Appointment():
    tkSetWindow = Toplevel(basis)
    tkSetWindow.title('Set Appointment')
    tkSetWindow.geometry('258x200')
    #Var for Entry
    hourVar = StringVar()
    minVar = StringVar()
    appointmentTagVar = StringVar()
    # Label for Time
    labelHour = Label(master=tkSetWindow, bg='#FFCFC9', text='Hour:')
    labelHour.place(x=54, y=24, width=100, height=27)
    labelMin = Label(master=tkSetWindow, bg='#FFCFC9', text='Min:')
    labelMin.place(x=54, y=54, width=100, height=27)
    # Entry for Time
    entryHour= Entry(tkSetWindow, bg='white', textvariable= hourVar)
    entryHour.place(x=164, y=24, width=50, height=27)
    entryMin= Entry(tkSetWindow, bg='white', textvariable= minVar)
    entryMin.place(x=164, y=54, width=50, height=27)
    # Label for Appointment
    labelAppointment= Label(master=tkSetWindow, bg='#FFCFC9', text='Appointment:')
    labelAppointment.place(x=54, y=84, width=100, height=27)
    # Entry for Appointment
    entryAppointment = Entry(tkSetWindow, bg='white', textvariable= appointmentTagVar)
    entryAppointment.place(x=164, y=84, width=90, height=27)
    #get Date
    date = cal.get_date()
    #Button
    setButton = Button(tkSetWindow, text = "Set Appointment")
    setButton.place(x=40, y=120, width=120, height=27)
    setButton['command'] = lambda:press_set_button(date, hourVar, minVar, appointmentTagVar, tkSetWindow)
    

#Window to view Appointments
def view_Appointment():
    #setup Window
    tkViewWindow = Toplevel(basis)
    tkViewWindow.title("View Appointments")
    tkViewWindow.geometry('500x500')
    TableMargin = Frame(tkViewWindow, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Date", "Time", "Appointment"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Date', text="Date", anchor=W)
    tree.heading('Time', text="Time", anchor=W)
    tree.heading('Appointment', text="Appointment", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()
    #check if calendar file exist
    try:
        with open ('./dockerfolder/myCal.csv', 'r') as mycal:
            reader = csv.DictReader(mycal, delimiter=',')
            for row in reader:
                date = row['Date']
                time = row['Time']
                ap = row['Appointment']
                tree.insert("", 0, values=(date, time, ap))
    except KeyError:
        tkViewWindow.destroy()
        return error_window(basis)



    

#Window to delete Appointment
def delete_Appointment():
    tkDeleteWindow = Toplevel(basis)
    tkDeleteWindow.title('Delete Appointment')
    tkDeleteWindow.geometry('258x200')
   #Var for Entry
    hourV = StringVar()
    minV = StringVar()
    appointmentTagVar = StringVar()
    # Label for Time
    labelHour = Label(master=tkDeleteWindow, bg='#FFCFC9', text='Hour:')
    labelHour.place(x=54, y=24, width=100, height=27)
    labelMin = Label(master=tkDeleteWindow, bg='#FFCFC9', text='Min:')
    labelMin.place(x=54, y=54, width=100, height=27)
    # Entry for Time
    entryHour= Entry(tkDeleteWindow, bg='white', textvariable= hourV)
    entryHour.place(x=164, y=24, width=50, height=27)
    entryMin= Entry(tkDeleteWindow, bg='white', textvariable= minV)
    entryMin.place(x=164, y=54, width=50, height=27)
    # Label for Appointment
    labelAppointment= Label(master=tkDeleteWindow, bg='#FFCFC9', text='Appointment:')
    labelAppointment.place(x=54, y=84, width=100, height=27)
    # Entry for Appointment
    entryAppointment = Entry(tkDeleteWindow, bg='white', textvariable= appointmentTagVar)
    entryAppointment.place(x=164, y=84, width=90, height=27)
    #get Date
    date = cal.get_date()
    #Button
    deleteButton = Button(tkDeleteWindow, text = "Delete Appointment")
    deleteButton.place(x=40, y=120, width=140, height=27)
    deleteButton['command'] = lambda:press_delete_button(date, hourV, minV, appointmentTagVar, tkDeleteWindow)
    
# Add Button and Label
Button(basis, text = "Set Appointment",
       command = set_Appointment).pack(pady = 10)
 
Button(basis, text = "Delete  Appointment",
       command = delete_Appointment).pack(pady = 10)

Button(basis, text = "View Appointment",
       command = view_Appointment).pack(pady = 10)   

date = Label(basis, text = "")
date.pack(pady = 20)
 
# Excecute Tkinter
basis.mainloop()