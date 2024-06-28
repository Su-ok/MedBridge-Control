## Messed the whole process of changing branch from Master to Main ##

Same project is available with the name [Hospital-Manager](https://github.com/Su-ok/Hospital-Manager) on my profile's repo section

### TOPIC: MedBridge Control

#### Requirements:
- Tkinter module: Used for GUI design.
- Mysql.connector module: Establishes connection with MySQL database and performs operations.
- MySQL Workbench

#### Instructions to Establish MySQL Connection:
1. Create a table named `hospital` in an existing or new database using MySQL Workbench.
2. Update the `conn` variable (host, username, password, database) at specific line numbers (145, 156, 168, 199) in the code according to your MySQL Workbench settings.
3. Ensure the `hospital` table has attributes: Reference_No (primary key), Nameoftablet, Dose, Issuedate, Expdate, Patientname. Reference_No should be INT, others VARCHAR(25).
4. Column names in the database table should match those used in SQL queries (update and delete) in the code.

#### Instructions to Run the Project:
1. Run the code to open a window labeled “HOSPITAL MANAGEMENT SYSTEM” with two sections: Patient Information and Prescription.
2. The bottom half displays a table with database contents after operations.
3. Use buttons in the middle frame: Prescription, Prescription Data, Update, Delete, Clear, Exit.
4. Enter values correctly based on attribute data types to avoid errors.
5. Button functionalities:
   - Prescription: Copies Patient Information to Prescription.
   - Prescription Data: Inserts data into the database.
   - Update: Updates a row based on Reference_No.
   - Delete: Deletes a row based on Reference_No.
   - Clear: Clears all entries.
   - Exit: Prompts to exit the window.

## Preferrably don't refer to this repo