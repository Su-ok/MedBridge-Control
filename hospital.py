''' 
    Group Members are:
    20BAI10015 -> Ashish Vats
    20BAI10268 -> Palak Garg
    20BAI10372 -> Deepak Kumar
    20BAI10373 -> Suchir Okram 
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Issuedate=StringVar()
        self.Expdate=StringVar()
        self.PatientName=StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("arial",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # ================Dataframe===========================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                                        font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=900,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                                        font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=910,y=5,width=560,height=350)

        # ================Buttons frame===========================================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        # ================Details frame===========================================
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        # ================DataframeLeft===========================================
        lblNameTablet=Label(DataframeLeft,font=("arial",22,"bold"),text="Names of Tablet:",padx=2,pady=6)
        lblNameTablet.grid(row=1,column=0,sticky=W)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=("arial",23,"bold"),width=34)
        comNametablet['values']=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=1,column=1)

        lblref=Label(DataframeLeft,font=("arial",22,"bold"),text="Reference no:",padx=2)
        lblref.grid(row=0,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",23,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=0,column=1)

        lblDose=Label(DataframeLeft,font=("arial",22,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",23,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblissueDate=Label(DataframeLeft,font=("arial",22,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("arial",23,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",22,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",23,"bold"),textvariable=self.Expdate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblPatientname=Label(DataframeLeft,font=("arial",22,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientname.grid(row=7,column=0,sticky=W)
        txtPatientname=Entry(DataframeLeft,font=("arial",23,"bold"),textvariable=self.PatientName,width=35)
        txtPatientname.grid(row=7,column=1)


        # =====================DataframeRight===================
        self.txtPrescription=Text(DataframeRight,font=("arial",13,"bold"),width=57,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        # =====================Buttons===================
        btnPrescription=Button(Buttonframe,command=self.iPrescription,text="Prescription",bg="blue",fg="white",font=("arial",12,"bold"),width=24,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="blue",fg="white",font=("arial",12,"bold"),width=24,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1) #

        btnUpdate=Button(Buttonframe,command=self.update_data,text="Update",bg="blue",fg="white",font=("arial",12,"bold"),width=24,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="blue",fg="white",font=("arial",12,"bold"),width=24,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="blue",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="blue",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        #======================Table==========================
        #======================Scrollbar=============================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("ref","nameoftablet","dose","issuedate",
                                "expdate","pname"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("ref",text="Reference no")
        self.hospital_table.heading("nameoftablet",text="Name of tablet")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Expt Date")
        self.hospital_table.heading("pname",text="Patient Name")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("nameoftablet",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("pname",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.put_on)
        self.get_db()
    
    #===================Functionality Declaration====================
    def iPrescriptionData(self): # to insert in the database table
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="saitama",database="db_movie")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s)",
                                        (self.ref.get(),self.Nameoftablets.get(),self.Dose.get(),
                                        self.Issuedate.get(),self.Expdate.get(),self.PatientName.get()))
        conn.commit()
        self.get_db()
        conn.close()
        messagebox.showinfo("Success","Record has been inserted")
    
    def update_data(self): # to update a row based on its Reference_No(primary key) in the database table
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="saitama",database="db_movie")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Nameoftablet=%s,Dose=%s,Issuedate=%s,Expdate=%s,Patientname=%s where Reference_No=%s",(
                self.Nameoftablets.get(),self.Dose.get(),self.Issuedate.get(),
                self.Expdate.get(),self.PatientName.get(),self.ref.get()
        ))
        conn.commit()
        self.get_db()
        conn.close()
        messagebox.showinfo("Update","Record has been updated successfully")
    
    def get_db(self): #to fetch all the data from the database table and display it in the table present(at the bottom) in the open window
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="saitama",database="db_movie")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        r=my_cursor.fetchall()
        if len(r)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in r:
                self.hospital_table.insert("",END,values=i)
        conn.commit()
        conn.close()

    def put_on(self,event=""): # to put on(focus) the data of the row(when clicked) on the dataframes according to the corresponding attributes' values
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.ref.set(row[0])
        self.Nameoftablets.set(row[1])
        self.Dose.set(row[2])
        self.Issuedate.set(row[3])
        self.Expdate.set(row[4])
        self.PatientName.set(row[5])

    def iPrescription(self): # to print all the values present in the left dataframe(patient information) onto the right dataframe(prescription)
        self.txtPrescription.insert(END,"Reference No:\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Name of Tablets:\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t"+self.Expdate.get()+"\n")
        self.txtPrescription.insert(END,"Patient name:\t\t"+self.PatientName.get()+"\n")

    def idelete(self): # to delete a row based on its Reference_No(primary key) in the database table 
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="saitama",database="db_movie")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.get_db()
        messagebox.showinfo("Delete","Patient details has been deleted successfully")

    def clear(self): # to clear everything written/entered in the dataframe
        self.ref.set("")
        self.Nameoftablets.set("")
        self.Dose.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.PatientName.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self): # to ask for permission to exit from the window
        iExit=messagebox.askyesno("Hospital management system","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return

root=Tk()
ob=Hospital(root)
root.mainloop()
