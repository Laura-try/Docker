# Import Required Library
from tkinter import *
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
myAppointment = ['Date', 'Time', 'Appointment']

# Create CSV-File
mycal = open('myCal.csv', 'w')
wr = csv.writer(mycal)
wr.writerow(myAppointment)
    
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())

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
   

    #Function to save Appointment
    time = entryTime.get()
    appointmentName = entryAppointment.get()
    date = cal.get_date()
    appointment = [date, time, appointmentName]
    def press_set_button(app):
        wr.writerow(app)
        tkSetWindow.destroy()

    #Button
    setButton = Button(tkSetWindow, text = "Set Appointment", command= press_set_button(appointment))
    setButton.place(x=145, y=76, width=90, height=27)
    
    



#Function to view Appointments
#def view_Appointment():
    

#Function to delete Appointment
#def delete_Appointment():
    tkDeleteWindow = Tk()
    tkDeleteWindow.title('Delete Appointment')
    tkDeleteWindow.geometry('258x100')
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
    #Function to delete Appointment
    time = float(entryTime.get())
    appointmentName = entryAppointment.get()
    date = cal.get_date()
    
  
    
#Function to close App
def closeApp():
    mycal.close()
    basis.destroy()  
 
# Add Button and Label
Button(basis, text = "Set Appointment",
       command = set_Appointment).pack(pady = 10)
 
Button(basis, text = "Delete  Appointment",
       command = grad_date).pack(pady = 10)

Button(basis, text = "View Appointment",
       command = grad_date).pack(pady = 10)   

Button(basis, text = "Close Calendar",
       command = closeApp).pack(pady = 10)  

date = Label(basis, text = "")
date.pack(pady = 20)
 
# Excecute Tkinter
basis.mainloop()