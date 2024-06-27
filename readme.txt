TOPIC: 	HOSPITAL MANAGEMENT SYSTEM

GROUP MEMBERS:
	20BAI10015 -> Ashish Vats
	20BAI10268 -> Palak Garg
	20BAI10372 -> Deepak Kumar
	20BAI10373 -> Suchir Okram


The following requirements must be present/installed in order to run our python project:
1. Tkinter module: It is used to design GUI that we have prepared in our project. 
2. Mysql.connector module: It is used to establish a connection of our project with mysql database present in the user’s device, which will simultaneously perform all the necessary operations in the database table at the backend.
3. Mysql Workbench


Instructions to establish mysql connection with our project:
1. First, you need to create a table, named hospital, in any existing database (you can create new database too) in your device’s mysql workbench.
2. Then, at the line numbers 145, 156, 168, 199 of the code, you need to give the specifications, i.e. host, username, password, and database, mentioned in the connection variable, “conn”, on the basis of your(user’s) device’s mysql workbench specifications.
3. The table created in the workbench must contain 6 attributes, namely Reference_No, Nameoftablet, Dose, Issuedate, Expdate, Patientname, with Reference_No being the primary key.
4. The datatype of Reference_No should be INT, and the datatype of the rest of the attributes should be VARCHAR(25).
5. The column names/attributes while creating the database table in the workbench should be same as the attributes written in the update query, i.e. "update hospital set Nameoftablet=%s,Dose=%s,Issuedate=%s,Expdate=%s,Patientname=%s where Reference_No=%s", at line number 158 of our code.
   This can be checked in the delete query also, i.e. "delete from hospital where Reference_No=%s", at line number 201 of our code.
6. After performing all these steps, your mysql connection will be set up.


Instructions to run our project code:
1. First, after running the code, you will see a window appearing with a label at the top center mentioning “HOSPITAL MANAGEMENT SYSTEM”. It’s top half containing dataframe with it’s left as Patient Information (containing the attributes that need to be entered) and it’s right as Prescription (which will be empty at first). It’s bottom half showing a table with all the attributes represented as columns, which will show all the contents of the database table after performing every database related operation.
2. Also, in between, there is a button frame too in the middle which has buttons named Prescription, Prescription Data, Update, Delete, Clear, and Exit.
3. Each button will work on the basis of their functions after filling/entering values corresponding to the attributes in the Patient Information dataframe.
4. Make sure to enter the values according to the corresponding attribute's datatype. Otherwise, it won't work and give an error.
5. Functionality of each button has been mentioned below:
  1) Prescription: to print all the values present in the left dataframe (Patient Information) onto the right dataframe (Prescription).
  2) Prescription Data: to insert in the database table.
  3) Update: to update a row based on its Reference_No( primary key) in the database table.
  4) Delete: to delete a row based on its Reference_No (primary key) in the database table.
  5) Clear: to clear everything written/entered in the dataframe.
  6) Exit: to ask for permission to exit from the window.
