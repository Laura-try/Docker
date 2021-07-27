# Import Required Library
from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import Calendar
import csv
 
# Create Object
basis = Tk()

# Set geometry
basis.geometry("400x400")
 

# Add Calendar
cal = Calendar(basis, selectmode = 'day')
 
cal.pack(pady = 20)

#Header for CVS-File
myAppointment = ['Date', 'Time', 'Tag']

# Create CSV-File
mycal = open('myCal.csv', 'w')
wr = csv.writer(mycal)
rd = csv.DictReader(mycal)
wr.writerow(myAppointment)
    

#Function for Set Button
def press_set_button(app,x):
    wr.writerow(app)
    x.destroy()

#Function for Delete Button
def press_delete_button(x):
    x.destroy()

def delete_row(date_entry, time_entry, tag_entry):
    for row in rd:
        if row['Date'] != date_entry and row['Time'] != time_entry and row['Tag'] != tag_entry:
            wr.writerow(row)

#Function to set Appointment
def set_Appointment():
    tkSetWindow = Toplevel(basis)
    tkSetWindow.title('Set Appointment')
    tkSetWindow.geometry('258x200')
    # Label for Time
    labelTime = Label(master=tkSetWindow, bg='#FFCFC9', text='Time:')
    labelTime.place(x=54, y=24, width=100, height=27)
    # Entry for Time
    entryTime = Entry(master=tkSetWindow, bg='white')
    entryTime.place(x=164, y=24, width=40, height=27)
    # Label for Appointment
    labelAppointment= Label(master=tkSetWindow, bg='#FFCFC9', text='Appointment:')
    labelAppointment.place(x=54, y=64, width=100, height=27)
    # Entry for Appointment
    entryAppointment = Entry(master=tkSetWindow, bg='white')
    entryAppointment.place(x=164, y=64, width=90, height=27)
   
    #Button
    setButton = Button(tkSetWindow, text = "Set Appointment")
    setButton.place(x=40, y=100, width=120, height=27)

    #Function to save Appointment
    time = entryTime.get()
    appointmentName = entryAppointment.get()
    date = cal.get_date()
    appointment = [date, time, appointmentName]

    setButton['command'] = lambda:press_set_button(appointment,tkSetWindow)
    
    



#Function to view Appointments
def view_Appointment():
    #setup Window
    tkViewWindow = Toplevel(basis)
    tkViewWindow.title("View Appointments")
    tkViewWindow.geometry('500x500')
    TableMargin = Frame(tkViewWindow, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Date", "Time", "Tag"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Date', text="Date", anchor=W)
    tree.heading('Time', text="Time", anchor=W)
    tree.heading('Tag', text="Tag", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()
    for row in rd:
        date = row['Date']
        time = row['Time']
        tag = row['Tag']
        tree.insert("", 0, values=(date, time, tag))


    

#Function to delete Appointment
def delete_Appointment():
    tkDeleteWindow = Tk()
    tkDeleteWindow.title('Delete Appointment')
    tkDeleteWindow.geometry('258x140')
    # Label for Time
    labelTime = Label(master=tkDeleteWindow, bg='#FFCFC9', text='Time:')
    labelTime.place(x=54, y=24, width=100, height=27)
    # Entry for Time
    entryTime = Entry(master=tkDeleteWindow, bg='white')
    entryTime.place(x=164, y=24, width=40, height=27)
    # Label for Appointment
    labelAppointment= Label(master=tkDeleteWindow, bg='#FFCFC9', text='Appointment:')
    labelAppointment.place(x=54, y=64, width=100, height=27)
    # Entry for Appointment
    entryAppointment = Entry(master=tkDeleteWindow, bg='white')
    entryAppointment.place(x=164, y=64, width=90, height=27)

    #Delete Button
    setButton = Button(tkDeleteWindow, text = "Delete Appointment")
    setButton.place(x=40, y=100, width=120, height=27)

    #Function to delete Appointment
    time = (entryTime.get())
    appointmentName = entryAppointment.get()
    date = cal.get_date()

    setButton['command'] = lambda:press_delete_button(tkDeleteWindow)
    
  
    
#Function to close App
def closeApp():
    mycal.close()
    basis.destroy()  
 
# Add Button and Label
Button(basis, text = "Set Appointment",
       command = set_Appointment).pack(pady = 10)
 
Button(basis, text = "Delete  Appointment",
       command = delete_Appointment).pack(pady = 10)

Button(basis, text = "View Appointment",
       command = view_Appointment).pack(pady = 10)   

Button(basis, text = "Close Calendar",
       command = closeApp).pack(pady = 10)  

date = Label(basis, text = "")
date.pack(pady = 20)
 
# Excecute Tkinter
basis.mainloop()