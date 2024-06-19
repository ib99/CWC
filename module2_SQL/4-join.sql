.system clear

--Now we'll put the previous concept together and learn how to pull data from multiple tables to search for specific patients.

--Let's write a statement that shows the patients' first name, last name and DOB along with their physician and pertinent office information. This will use a JOIN statement to combine the patients and physicians tables.

--Refer back to the main.sql file for column/variable names that you may need.
--We will use 'p' and 'ph' as aliases for the patients and physicians tables respectively.  
  
SELECT 
/*insert variables*/
    p.first_name AS patient_first_name, 
    p.last_name AS patient_last_name,
    p.date_of_birth AS patient_dob,
    ph.physician_name AS physician_name,
    ph.office_city,
    ph.office_state,
    ph.physician_id AS physician_id
FROM 
    patients AS p
JOIN 
    physicians AS ph
ON 
    /*write the statement to match foreign keys here using p."key"=ph."key"*/
    p.primary_care_physician_id = ph.physician_id;

.print "------------------------------------------------------"
.print
  
--Finally we want to find all patients who see doctors based in California who are specialized in either cardiology or pulmonology. Have the query show the patients' name, DOB, the physician's name, and the physician's office city.

/*-statement here-*/
SELECT 
/*insert variables*/
    p.first_name AS patient_first_name, 
    p.last_name AS patient_last_name,
    p.date_of_birth AS patient_dob,
    ph.physician_name AS physician_name,
    ph.office_city,
    ph.office_state,
    ph.physician_id AS physician_id
FROM 
    patients p
JOIN 
    physicians ph
ON 
    /*key statement here*/
    primary_care_physician_id = ph.physician_id
WHERE 
    /*filter statement to select the appropriate state and specialty criteria*/
   office_state = 'CA' AND primary_specialty IN ('Cardiology', 'Pulmonology')


/* Use ".read 4-join.sql" to see the results. */

-------------------------------------------------------------
/*CONGRATS! You've completed this exercise. For more involved learning, SQLZoo is a quick and easy resource: https://sqlzoo.net/wiki/SQL_Tutorial

Also, please comment in Slack with questions or comments for the discussion around SQL and databases.*/