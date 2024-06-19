.system clear 
--This command clears the console each time this exercise is run
  
/* For the first exercise, we will work with the basic CRUD operations.
C = Create
R = Read
U = Update
D = Delete
*/

/*Using the information from the tables reviewed in the intro file, write statements to:
1. Add a patient to the database
2. Read that patient using "WHERE id = [the patiend's id]"
3. Update the patient's primary diagnosis to "Case of the Mondays"
4. Read the patient again to confirm the update
5. Delete the patient using the id
6. Read the patient table again to confirm the deletion
*/

--This statement is an example to get you started, please adjust as you see fit before running the insert and complete other statements below the insertion
INSERT INTO patients VALUES(12, 'John', 'Brown', '1932-05-03', 'M', 'Feels Bad', 107, 'Dr. Sophia Miller'), (13, 'George', 'Washington', '1945-01-01', 'M', 'Feels ok', 106, 'Dr. Michael Wilson');

--Add a patient to the database, use an id greater than 12 to avoid conflict errors with existing patients. Physician IDs range from 101 to 111 with details in main.sql.

.print "------------------------------------------------------"
.print
--(these print statements add space and readability to the output)
  
--Read that patient using "WHERE id = [the patiend's id]"
SELECT * FROM patients WHERE /*finish the statement here*/
id = 13 ;

.print
--readability space again
  
--Update the patient's primary diagnosis to "Case of the Mondays"
UPDATE patients SET /*finish statement here*/
primary_diagnosis = 'Case of the Mondays'
WHERE id = 13;

.print

--Read the patient again to confirm the update  
SELECT * /*complete the statement here*/
FROM patients WHERE id = 13;

.print

--Delete the patient using the id
DELETE FROM patients
where id = 13/*finish statement here*/;
.print "Patient Deleted\n"
  
--Read the patient table again to confirm the deletion
SELECT * FROM patients;

--IMPORTANT--
/*** You will type ".read 2-crud.sql" into the console to see a single output for the entire exercise. 

You will not use the "Shell" tab at all during these exercises
***/


------------------