from tkinter import *
from tkinter import messagebox
from random import randint, randrange
import tkinter.ttk as ttk
import datetime
import os


import sqlite3

#Make the Main Window
window = Tk()

#Set the Geometry
window.geometry("1450x400")
window.title("Patient Check in")

path= os.getcwd()+ '\\'

#"C:/Users/frank/OneDrive/Desktop/CISP71_Tkinter_SQLite_Examples/"

#Adding Patient Notes feature
conn_notes = sqlite3.connect(path+ "notes.db")
c_notes = conn_notes.cursor()

#Creating the table to store the notes


c_notes.execute('''
CREATE TABLE IF NOT EXISTS patient_notes (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    date TEXT,
    notes TEXT
);
''')




#Creating the Table for patients in Patient Database
conn_patientDatabase = sqlite3.connect((path+ "patientDatabase.db"))
c_patientDatabase = conn_patientDatabase.cursor()

#Now Create the database

c_patientDatabase.execute('''
CREATE TABLE IF NOT EXISTS patients (
	"patient_id"	INTEGER,
	"patientFirstName"	TEXT,
	"patientLastName"	TEXT,
	"patientDOB"	TEXT,
	"patientCity"	TEXT,
	"patientState"	TEXT,
	"patientZipCode"	INTEGER,
	"patientStatus"	TEXT,
	PRIMARY KEY("patient_id","patientFirstName")
);
''')
conn_patientDatabase.close()
#  int(patient_id),
#             pateintFirstNameEn.get(),patientLastNameEn.get(),patientDOBen.get(),
#             patientCityEn.get(), selected.get(), int(patientZipCodeEn.get())

#Function to add a note for a patient
def add_note():
    selected_item = tvPatient.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a patient first")
        return
    
    
    patient_id = tvPatient.item(selected_item[0], 'values')[0]
    note_text = note_entry.get()
    
    
    if note_text:
        conn = sqlite3.connect((path + "notes.db"))
        c = conn.cursor()
        c.execute("INSERT INTO patient_notes (patient_id, date, notes) VALUES (?, ?, ?)",
                  (patient_id, datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S"), note_text)
                  
                  )
        conn.commit()
        conn.close()
        note_entry.delete(0,END)
        show_notes_for_selected_patient()
        
        
def show_notes_for_selected_patient():
    selected_item = tvPatient.selection()
    if not selected_item:
        return
    
    patient_id = tvPatient.item(selected_item[0], 'values')[0]
    
    for item in tvNotes.get_children():
        tvNotes.delete(item)
    
    conn = sqlite3.connect(path + "notes.db")
    c = conn.cursor()
    c.execute("SELECT date, notes FROM patient_notes WHERE patient_id = ? ORDER BY date DESC", (patient_id,))
    notes = c.fetchall()
    conn.close()
    
    for note in notes:
        tvNotes.insert("", 'end', values=(note[0], note[1]))
        


#Adding a Search Patient Feature

class InputDialog(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Enter Patient Details")
        
        self.result = None
        
        Label(self, text="Last Name:").grid(row=0, column=0)
        self.last_name_entry = Entry(self)
        self.last_name_entry.grid(row=0, column=1)
        
        Label(self, text="DOB MM/DD/YYYY: " ).grid(row=1, column=0)
        self.dob_entry = Entry(self)
        self.dob_entry.grid(row=1, column=1)
        
        Button(self, text="Submit", command=self.on_submit).grid(row=2, column=0, columnspan=2)

    
    def on_submit(self):
        last_name = self.last_name_entry.get()
        dob = self.dob_entry.get()
        
        if last_name and dob:
            self.result = last_name, dob
            self.destroy()
        else:
            messagebox.showwarning("Input Error", "Please enter boith last name and date of birth")
     
def search_patient():
    dialog = InputDialog(window)
    window.wait_window(dialog)
    
    if dialog.result:
        last_name, dob = dialog.result
        conn = sqlite3.connect(path+"patientDatabase.db")
        c = conn.cursor()
        query = "SELECT * FROM patients WHERE patientLastName = ? AND patientDOB = ?"
        c.execute(query, (last_name, dob))
        result = c.fetchone()
        conn.close()
        
        if result:
            clearFields()
            pateintFirstNameEn.insert(0, result[0])
            patientLastNameEn.insert(0, result[1])
            patientDOBen.insert(0, result[2])
            patientCityEn.insert(0, result[3])
            selected.set(result[4])
            patientZipCodeEn.insert(0, result[5])
        else:
            messagebox.showinfo("Info", "No patient found with the given last name and date of birth")
#---------------------------------------------------


#TODO Add functions here but assign the command for the buttons and stuff 
def display_message_box(text):
    messagebox.showinfo("Info:", text)


def addrecord_and_update_TreeView():
    addRecord()
    displayRecords()




def clearFields():
    patientsIDEn.delete(0, END)
    pateintFirstNameEn.delete(0,END)
    patientLastNameEn.delete(0, END)
    patientDOBen.delete(0, END)
    patientCityEn.delete(0, END)
    
    patientZipCodeEn.delete(0, END)
    selected.set(stateList[4])
    
    
    
#add function to add record and display the records
    #connect to a database if not found it will create one
    #use this placeholder variales and and a dictionary
    #Make sure to use the try catch as if this fails itll crash the whole program
def updatePatient():
    conn = sqlite3.connect(path + 'patientDatabase.db')
    c = conn.cursor()

    c.execute('''UPDATE patients SET
              patientFirstName = ?,
              patientLastName = ?,
              patientDOB = ?,
              patientCity = ?,
              patientState = ?,
              patientZipCode = ?,
              patientStatus = ?  -- Add this line to update patientStatus
              WHERE patient_id = ?
                    ''',
              (pateintFirstNameEn.get(), patientLastNameEn.get(),patientDOBen.get(),patientCityEn.get(),
               selected.get(),int(patientZipCodeEn.get()), radio_var.get(), patientsIDEn.get()))  # Get radio button value
    conn.commit()
    conn.close()

def updatePatient_and_updatetheTV():
    updatePatient()
    displayRecords()

def addRecord():
    conn = sqlite3.connect(path + "patientDatabase.db")
    try:
        patient_id = randrange(100, 999)
        c = conn.cursor()
        selected_status = radio_var.get()  # Get the selected status from the radio buttons
        c.execute("INSERT INTO patients VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (
            int(patient_id),
            pateintFirstNameEn.get(), patientLastNameEn.get(), patientDOBen.get(),
            patientCityEn.get(), selected.get(), int(patientZipCodeEn.get()), selected_status
        ))
        conn.commit()
        print("One record of patient added successfully")
    except sqlite3.Error as e:
        display_message_box("Error: " + str(e))
        print("Error: ", e)
    finally:
        conn.close()
    clearFields()

def displayRecords():
    #tvPatient.dekete(*window.tvPatient.get_children()) # clears the treeview tvPatient
    
    #loop over the children of the treeview Patient object
    
    for row in tvPatient.get_children():
        tvPatient.delete(row)
    
    conn = sqlite3.connect(path+"patientDatabase.db")
    c = conn.cursor()
    c.execute("select *,oid from patients")
    rows = c.fetchall()
    
    for row in rows:
        patientId = row[0]
        First_Name = row[1]
        Last_Name = row[2]
        Address = row[3]
        City = row[4]
        State = row[5]
        ZipCode = row[6]
        Status = row[7]
        tvPatient.insert("",'end', text=id, values=(patientId,First_Name,Last_Name,Address,City,
                                                    State, ZipCode,Status, id))

def deleteRecord():

    #connect to the database
    #use placeholder variables and a dictionary
    conn = sqlite3.connect((path+"patientDatabase.db"))
    #This is the code we will send to the database
    qry="DELETE from patients where patientFirstName = ?;"
    
    try:
        c = conn.cursor()
        c.execute(qry, (pateintFirstNameEn.get(),))
        conn.commit()
        print("record deleted successfully")
    except:
        print("Error in deleting record")
        conn.rollback()
    conn.close()
    clearFields()

def delete_then_display():
    deleteRecord()
    displayRecords()
    
def show_selected_record(event):
    clearFields()
    show_notes_for_selected_patient()
    for selection in tvPatient.selection():
        item = tvPatient.item(selection)
        global id
        patID,fName,lName,address,city,state,zipCode, patientStatus = item["values"][0:8]
        patientsIDEn.insert(0,patID)
        pateintFirstNameEn.insert(0,fName)
        patientLastNameEn.insert(0,lName)
        patientDOBen.insert(0,address)
        patientCityEn.insert(0, city)
        selected.set(state) #<----- TODO make this so when a record is selected it autofills the state thats in the database or rather the treeview
        patientZipCodeEn.insert(0,zipCode)
        radio_var.set(patientStatus)
        
    
        
    return id    



#Create the List of States
stateList=["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY" ]

#Assign the return type of the selected state type since its letters its a String
selected = StringVar()

#to set the default value you can you use the .set on the selected

selected.set(stateList[4])

#Space for the labels Havent Placed them yet will do them later
patientIDLb = Label(window, text="Patients ID")
patientFirstNameLb = Label(window, text="Patient First Name")
patientLastNameLb = Label(window, text="Patients Last Name")
patientDOBLb = Label(window, text="DOB MM/DD/YYYY")
patientCityLb = Label(window, text="City")
patientStateLb = Label(window,text="State")
patientZipCodeLb = Label(window, text="Zip Code")

patientNoteLb = Label(window, text="Note Entry")
#-------------------------

#Now make the entry widgets for the labels 
patientsIDEn = Entry(window)
pateintFirstNameEn = Entry(window)
patientLastNameEn = Entry(window)
patientDOBen = Entry(window)
patientCityEn = Entry(window)
patientZipCodeEn = Entry(window)
#---------------------------------------------------------

#This is where Ill make the OptionMenu Widget for the drop list
#*stateList is to unpack the whole list that we declared which is the list of states

stateOp = OptionMenu(window, selected, *stateList)

#Radio Buttons are created here

radio_var = StringVar()

#Creating the wdiget of the radio button
checkedInRdBTN = Radiobutton(window, text="Checked in", variable= radio_var, value="Checked In")
notCheckedInRdBTN = Radiobutton(window, text="Not Checked in", variable=radio_var, value="Not Checked In")
#Quickly Placing the Radio Buttons
checkedInRdBTN.grid(row=1, column=2)
notCheckedInRdBTN.grid(row=2, column=2)




#Buttton Widgets Creation 

addbtn = Button(window, text="Add Record", command=addrecord_and_update_TreeView)

displaybtn = Button(window, text="Display Records", command= displayRecords)
deletebtn = Button(window, text="Delete Record", command=delete_then_display)
updatebtn = Button(window, text="Update Patient", command=updatePatient_and_updatetheTV)

findPatient = Button(window,text="Find Patient", command=search_patient)

#Now we place Labels
patientIDLb.grid(row=0, column=2)
patientFirstNameLb.grid(row=0,column=0)
patientLastNameLb.grid(row=1,column=0)
patientDOBLb.grid(row=2,column=0)
patientCityLb.grid(row=3, column=0)
patientStateLb.grid(row=4,column=0)
patientZipCodeLb.grid(row=5,column=0)

patientNoteLb.grid(row=12, column=0)

#Now Placing the Entries and other stuffs
patientsIDEn.grid(row=0, column=3)
pateintFirstNameEn.grid(row=0,column=1)
patientLastNameEn.grid(row=1,column=1)
patientDOBen.grid(row=2,column=1)
patientCityEn.grid(row=3,column=1)
#OptionList
stateOp.grid(row=4,column=1)
#OptionList
patientZipCodeEn.grid(row=5,column=1)


#Specify where I want the Buttons to go
addbtn.grid(row=7,column=0)
deletebtn.grid(row=8,column=1)
updatebtn.grid(row=7,column=1)
displaybtn.grid(row=8,column=0)
findPatient.grid(row=8, column=2)
#---------------------------------------------------------
#---------------------------------------------------------

#Treeview widget
#specify a tuple columns
columns = ("#1","#2","#3","#4","#5","#6",'#7', '#8')

tvPatient = ttk.Treeview(window,show="headings", height="5", columns=columns)

#specify the heading to the corresponding headings


tvPatient.heading('#1', text="Patient ID", anchor='center')
tvPatient.column('#1',width=50, anchor='center',stretch=True)

tvPatient.heading('#2', text="First Name", anchor='center')
tvPatient.column('#2', width=50, anchor='center', stretch=True)

tvPatient.heading('#3', text="Last Name", anchor='center')
tvPatient.column('#3', width=50, anchor='center', stretch=True)

tvPatient.heading('#4', text="DOB", anchor='center')
tvPatient.column('#4', width=50, anchor='center', stretch=True)

tvPatient.heading('#5', text="City", anchor='center')
tvPatient.column('#5', width=50, anchor='center', stretch=True)

tvPatient.heading('#6', text="State", anchor='center')
tvPatient.column('#6', width=50, anchor='center', stretch=True)

tvPatient.heading('#7', text="ZipCode", anchor='center')
tvPatient.column('#7', width=50, anchor='center', stretch=True)

tvPatient.heading('#8',text="Status", anchor="center")
tvPatient.column('#8',width=50, anchor="center",stretch=True)

#Notes Tree view Object
notes_columns = ("#1", "#2", "3")
tvNotes = ttk.Treeview(window, show="headings", height="5", columns=notes_columns)

tvNotes.heading('#1', text="Date", anchor='center')
tvNotes.column('#1', width=150, anchor='center', stretch=True)

tvNotes.heading('#2', text="Note", anchor='center')
tvNotes.column('#2', width=300, anchor="center", stretch=True)

# Entry and Button for adding notes

note_entry = Entry(window, width=50)
add_note_btn = Button(window, text="Add Note", command=add_note)

#Placing the Notes Entry and Button

note_entry.grid(row=12, column=3, columnspan=4)
add_note_btn.grid(row=12, column=2)

#----------------------------------------------

    
#Bind the tree view to the function show_selected_record
#Bind the Notes Tree View to the on_item_selected
tvPatient.bind("<<TreeviewSelect>>", show_selected_record)

tvPatient.grid(row=10,column=0,columnspan=10)


tvNotes.grid(row=10, column=10, columnspan=5)


displayRecords()
mainloop()