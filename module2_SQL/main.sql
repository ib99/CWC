.print "Hello, this is the initial setup for the SQL database"
.print "------------------------------------------------------"

--This is an example of how to create a table:
CREATE TABLE patients (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    gender CHAR(1),
    primary_diagnosis VARCHAR(100),
    primary_care_physician_id INT,
    primary_care_physician_name VARCHAR(50)
);

INSERT INTO patients (id, first_name, last_name, date_of_birth, gender, primary_diagnosis, primary_care_physician_id, primary_care_physician_name) VALUES
(1, 'John', 'Doe', '1985-03-25', 'M', 'Hypertension', 101, 'Dr. Sarah Connor'),
(2, 'Jane', 'Smith', '1990-07-14', 'F', 'Diabetes', 102, 'Dr. John Smith'),
(3, 'Michael', 'Brown', '1978-11-02', 'M', 'Asthma', 103, 'Dr. Emma Brown'),
(4, 'Emily', 'Johnson', '2000-05-18', 'F', 'Migraine', 104, 'Dr. William Johnson'),
(5, 'Matthew', 'Davis', '1965-09-30', 'M', 'Arthritis', 105, 'Dr. Olivia Davis'),
(6, 'Olivia', 'Wilson', '1982-12-21', 'F', 'Heart Disease', 106, 'Dr. Michael Wilson'),
(7, 'James', 'Miller', '1995-04-10', 'M', 'Depression', 107, 'Dr. Sophia Miller'),
(8, 'Sophia', 'Taylor', '1988-08-16', 'F', 'Allergies', 108, 'Dr. James Taylor'),
(9, 'William', 'Anderson', '1972-01-05', 'M', 'Chronic Pain', 109, 'Dr. Linda Anderson'),
(10, 'Ava', 'Thomas', '2001-06-27', 'F', 'Anxiety', 110, 'Dr. Robert Thomas'),
(11, 'James', 'Brown', '1933-05-03', 'M', 'Feels Good', 107, 'Dr. Sophia Miller');

.print "Patients table created successfully"
.print "------------------------------------------------------\n"
SELECT * FROM patients;
    
CREATE TABLE physicians (
    physician_id INT PRIMARY KEY,
    physician_name VARCHAR(50),
    primary_specialty VARCHAR(50),
    office_city VARCHAR(50),
    office_state VARCHAR(2)
);
    
INSERT INTO physicians (physician_id, physician_name, primary_specialty, office_city, office_state) VALUES
(101, 'Dr. Sarah Connor', 'Cardiology', 'Los Angeles', 'CA'),
(102, 'Dr. John Smith', 'Endocrinology', 'New York', 'NY'),
(103, 'Dr. Emma Brown', 'Pulmonology', 'Fresno', 'CA'),
(104, 'Dr. William Johnson', 'Neurology', 'Houston', 'TX'),
(105, 'Dr. Olivia Davis', 'Rheumatology', 'Amarillo', 'TX'),
(106, 'Dr. Michael Wilson', 'Cardiology', 'Washington', 'DC'),
(107, 'Dr. Sophia Miller', 'Psychiatry', 'Seattle', 'WA'),
(108, 'Dr. James Taylor', 'Allergy and Immunology', 'Miami', 'FL'),
(109, 'Dr. Linda Anderson', 'Pain Management', 'Buffalo', 'NY'),
(110, 'Dr. Robert Thomas', 'Psychiatry', 'Hershey', 'PA'),
(111, 'Dr. Who', 'Time Lord', 'Gallifrey', 'UK');

.print "------------------------------------------------------"
.print "Physicians table created successfully"
.print "------------------------------------------------------\n"

SELECT * FROM physicians;
.print "------------------------------------------------------"

.print "Databases ready to start exercises, enter '.system clear' to clear the console then open the intro.sql file for further instruction.\n"