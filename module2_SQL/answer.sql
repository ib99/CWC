--CRUD
INSERT INTO patients VALUES(12, 'John', 'Brown', '1932-05-03', 'M', 'Feels Bad', 107, 'Dr. Sophia Miller');

SELECT * FROM patients WHERE id = 12;

UPDATE patients SET primary_diagnosis = 'Case of the Mondays' WHERE id = 12;

SELECT * FROM patients WHERE id = 12;
DELETE FROM patients WHERE id = 12;

SELECT * FROM patients;

--Sort
SELECT physician_name, primary_specialty, office_state FROM physicians ORDER BY office_state;

SELECT * from physicians 
WHERE 
physician_name LIKE 'Dr. W%' AND
office_city LIKE 'G%';

SELECT * FROM patients WHERE 
date_of_birth BETWEEN '1930-01-01' AND '1980-12-31';

--Join
SELECT 
    p.first_name AS patient_first_name,
    p.last_name AS patient_last_name,
    p.date_of_birth,
    ph.office_city,
    ph.office_state
FROM 
    patients AS p
JOIN 
    physicians AS ph
ON 
    p.primary_care_physician_id = ph.physician_id;




