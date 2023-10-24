from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x650+0+0")

        #variables for DB
        self.NameOfTablets=StringVar()
        self.Ref=StringVar()
        self.Dose=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpiryDate=StringVar()
        self.SideEffect=StringVar()
        self.DailyDose=StringVar()
        self.BloodPressure=StringVar()
        self.NHSNumber=StringVar()
        self.PatientID=StringVar()
        self.Medication=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",
                       fg="blue",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #******************DataFrame***********
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1270,height=300)

        #******************Left DataFrame***********
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                             font=("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=850,height=250)

        #******************Right DataFrame***********
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                             font=("arial",12,"bold"),text="Prescription")
        DataframeRight.place(x=860,y=5,width=360,height=250)

        #******************Button DataFrame***********
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=440,width=1270,height=70)

        #******************Details DataFrame***********
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=515,width=1270,height=120)

        #******************DataFrame Left***********
        lblNameTablet=Label(DataframeLeft,font=("arial",12,"bold"),text="Names of Tablet",padx=2,pady=4)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.NameOfTablets,font=("arial",12,"bold"),width=28)
        comNametablet["values"]=("Nice","Corona Vaccine","Ativan","Adderall")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,text="Reference No",font=("arial",12,"bold"),padx=2,pady=4)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,textvariable=self.Ref,font=("arial",12,"bold"),width=30)
        txtref.grid(row=1,column=1)
        
        lblDose=Label(DataframeLeft,text="Dose",font=("arial",12,"bold"),padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,textvariable=self.Dose,font=("arial",12,"bold"),width=30)
        txtDose.grid(row=2,column=1)

        lblLot=Label(DataframeLeft,text="Lot",font=("arial",12,"bold"),padx=2,pady=4)
        lblLot.grid(row=3,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,textvariable=self.Lot,font=("arial",12,"bold"),width=30)
        txtLot.grid(row=3,column=1)

        lblissueDate=Label(DataframeLeft,text="Issue Date",font=("arial",12,"bold"),padx=2,pady=4)
        lblissueDate.grid(row=4,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,textvariable=self.IssueDate,font=("arial",12,"bold"),width=30)
        txtissueDate.grid(row=4,column=1)

        lblExpDate=Label(DataframeLeft,text="Expiry Date",font=("arial",12,"bold"),padx=2,pady=4)
        lblExpDate.grid(row=5,column=0,sticky=W)
        txtExpdate=Entry(DataframeLeft,textvariable=self.ExpiryDate,font=("arial",12,"bold"),width=30)
        txtExpdate.grid(row=5,column=1)

        lblSideEffect=Label(DataframeLeft,text="Side Effect",font=("arial",12,"bold"),padx=2,pady=4)
        lblSideEffect.grid(row=6,column=0,sticky=W)
        txtSideEfefct=Entry(DataframeLeft,textvariable=self.SideEffect,font=("arial",12,"bold"),width=30)
        txtSideEfefct.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,text="Daily Dose",font=("arial",12,"bold"),padx=2,pady=4)
        lblDailyDose.grid(row=0,column=2,sticky=W,)
        txtDailyDose=Entry(DataframeLeft,textvariable=self.DailyDose,font=("arial",12,"bold"),width=30)
        txtDailyDose.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,text="Blood Pressure",font=("arial",12,"bold"),padx=2,pady=4)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,textvariable=self.BloodPressure,font=("arial",12,"bold"),width=30)
        txtBloodPressure.grid(row=1,column=3)

        lblNhsNumber=Label(DataframeLeft,text="NHS Number",font=("arial",12,"bold"),padx=2,pady=4)
        lblNhsNumber.grid(row=2,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,textvariable=self.NHSNumber,font=("arial",12,"bold"),width=30)
        txtNhsNumber.grid(row=2,column=3)

        lblPatientId=Label(DataframeLeft,text="Patient ID",font=("arial",12,"bold"),padx=2,pady=4)
        lblPatientId.grid(row=3,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,textvariable=self.PatientID,font=("arial",12,"bold"),width=30)
        txtPatientId.grid(row=3,column=3)

        lblMedication=Label(DataframeLeft,text="Medication",font=("arial",12,"bold"),padx=2,pady=4)
        lblMedication.grid(row=4,column=2,sticky=W)
        txtMedication=Entry(DataframeLeft,textvariable=self.Medication,font=("arial",12,"bold"),width=30)
        txtMedication.grid(row=4,column=3)


        lblDateOfBirth=Label(DataframeLeft,text="Date of Birth",font=("arial",12,"bold"),padx=2,pady=4)
        lblDateOfBirth.grid(row=5,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,textvariable=self.DateOfBirth,font=("arial",12,"bold"),width=30)
        txtDateOfBirth.grid(row=5,column=3)

        lblPatientAddress=Label(DataframeLeft,text="Patient Address",font=("arial",12,"bold"),padx=2,pady=4)
        lblPatientAddress.grid(row=6,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,textvariable=self.PatientAddress,font=("arial",12,"bold"),width=30)
        txtPatientAddress.grid(row=6,column=3)

        #******************Left DataFrame***********
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=35,height=10.4,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #******************Adding Buttons***********
        btnPrescription=Button(Buttonframe,command=self.iPrecription, text="Prescription",bg="green",
                               font=("arial",12,"bold"),width=23,height=1)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe, command=self.iPrescriptionData, text="Prescription Data",bg="green",font=("arial",12,"bold"),width=20,height=1)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.update_data,text="Update",bg="green",font=("arial",12,"bold"),width=20,height=1)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.iDelete, text="Delete",bg="green",font=("arial",12,"bold"),width=20,height=1)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.clear, text="Clear",bg="green",font=("arial",12,"bold"),width=20,height=1)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,command=self.exit, text="Exit",bg="green",font=("arial",12,"bold"),width=14,height=1)
        btnExit.grid(row=0,column=5)

        #******************Table********************
        #**************Scroll Bar***********
        scroll_x=Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("NameOfTablets","Ref","Dose","Lot",
            "IssueDate","ExpiryDate","SideEffect","DailyDose","BloodPressure",
            "NHSNumber","PatientID","Medication","DateOfBirth","PatientAddress"),
            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("NameOfTablets", text = "Name of Tablet")
        self.hospital_table.heading("Ref", text="Reference No")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("Lot", text="Lot")
        self.hospital_table.heading("IssueDate", text="Issue Date")
        self.hospital_table.heading("ExpiryDate", text="Expiry Date")
        self.hospital_table.heading("SideEffect", text="Side Effect")
        self.hospital_table.heading("DailyDose", text="Daily Dose")
        self.hospital_table.heading("BloodPressure", text="Blood Pressure")
        self.hospital_table.heading("NHSNumber", text="NHS Number")
        self.hospital_table.heading("PatientID", text="Patient ID")
        self.hospital_table.heading("Medication", text="Medication")
        self.hospital_table.heading("DateOfBirth", text="Date of Birth")
        self.hospital_table.heading("PatientAddress", text="Patient Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("NameOfTablets", width=10)
        self.hospital_table.column("Ref", width=10)
        self.hospital_table.column("Dose", width=10)
        self.hospital_table.column("Lot", width=10)
        self.hospital_table.column("IssueDate", width=10)
        self.hospital_table.column("ExpiryDate", width=10)
        self.hospital_table.column("SideEffect", width=10)
        self.hospital_table.column("DailyDose", width=10)
        self.hospital_table.column("BloodPressure", width=10)
        self.hospital_table.column("NHSNumber", width=10)
        self.hospital_table.column("PatientID", width=10)
        self.hospital_table.column("Medication", width=10)
        self.hospital_table.column("DateOfBirth", width=10)
        self.hospital_table.column("PatientAddress", width=10)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #**************Functionality/column declaration**********
    def iPrescriptionData(self):
        if self.NameOfTablets.get() == "" or self.Ref.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='test',database='mydata')
            print(conn.is_connected)
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                  (self.NameOfTablets.get(),
                   self.Ref.get(),
                   self.Dose.get(),
                   self.Lot.get(),
                   self.IssueDate.get(),
                   self.ExpiryDate.get(),
                   self.SideEffect.get(),
                   self.DailyDose.get(),
                   self.BloodPressure.get(),
                   self.NHSNumber.get(),
                   self.PatientID.get(),
                   self.Medication.get(),
                   self.DateOfBirth.get(),
                   self.PatientAddress.get()))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")
    def update_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='test',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute("UPDATE hospital SET NameOfTablets=%s,Ref=%s, Dose=%s, Lot=%s, IssueDate=%s, ExpiryDate=%s, SideEffect=%s, DailyDose=%s, BloodPressure=%s, NHSNumber=%s, Medication=%s, DateOfBirth=%s, PatientAddress=%s WHERE  PatientID=%s", 
                          (self.NameOfTablets.get(),
                            self.Ref.get(),
                            self.Dose.get(),
                            self.Lot.get(),
                            self.IssueDate.get(),
                            self.ExpiryDate.get(),
                            self.SideEffect.get(),
                            self.DailyDose.get(),
                            self.BloodPressure.get(),
                            self.NHSNumber.get(),
                            self.Medication.get(),
                            self.DateOfBirth.get(),
                            self.PatientAddress.get(),
                            self.PatientID.get()))
        conn.commit()
        conn.close()
        self.clear()
        self.fetch_data()
        messagebox.showinfo("Success", "Record has been updated")

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='test',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #***** to highlight selected row
    def get_cursor(self,event):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.NameOfTablets.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2])
        self.Lot.set(row[3])
        self.IssueDate.set(row[4])
        self.ExpiryDate.set(row[5])
        self.SideEffect.set(row[6])
        self.DailyDose.set(row[7])
        self.BloodPressure.set(row[8])
        self.NHSNumber.set(row[9])
        self.PatientID.set(row[10])
        self.Medication.set(row[11])
        self.DateOfBirth.set(row[12])
        self.PatientAddress.set(row[13])

    def iPrecription(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.NameOfTablets.get()+"\n")
        self.txtPrescription.insert(END, "Name of Tablets:\t\t\t" + self.NameOfTablets.get() + "\n")
        self.txtPrescription.insert(END, "Reference No:\t\t\t" + self.Ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.IssueDate.get() + "\n")
        self.txtPrescription.insert(END, "Expiry Date:\t\t\t" + self.ExpiryDate.get() + "\n")
        self.txtPrescription.insert(END, "Side Effect:\t\t\t" + self.SideEffect.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Blood Pressure:\t\t\t" + self.BloodPressure.get() + "\n")
        self.txtPrescription.insert(END, "NHS Number:\t\t\t" + self.NHSNumber.get() + "\n")
        self.txtPrescription.insert(END, "Patient ID:\t\t\t" + self.PatientID.get() + "\n")
        self.txtPrescription.insert(END, "Medication:\t\t\t" + self.Medication.get() + "\n")
        self.txtPrescription.insert(END, "Date of Birth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address:\t\t\t" + self.PatientAddress.get() + "\n")

    def iDelete(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='test', database='mydata')
        my_cursor = conn.cursor()
        query="delete from hospital where PatientID=%s"
        value=(self.PatientID.get(),) 
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient record deleted successfully")
        self.clear()
        self.fetch_data()

    def clear(self):
        self.NameOfTablets.set('')
        self.Ref.set('')
        self.Dose.set('')
        self.Lot.set('')
        self.IssueDate.set('')
        self.ExpiryDate.set('')
        self.SideEffect.set('')
        self.DailyDose.set('')
        self.BloodPressure.set('')
        self.NHSNumber.set('')
        self.PatientID.set('')
        self.Medication.set('')
        self.DateOfBirth.set('')
        self.PatientAddress.set('')
        self.txtPrescription.delete(1.0, END)

    def exit(self):
        res = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if res >0:
            root.destroy()
            return
            
root = Tk()
ob = Hospital(root)
root.mainloop()