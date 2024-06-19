/* (comments look slightly different in SQL)
Due to some idiosyncracies with Replit and how SQL is handled here, you will not run these exercises in quite the same way as before. 

Replit has the green "run" button hard mapped to run the contents of "main.sql." So, if you rename or otherwise adjust that file, the exercises may not function correctly.

You will not run this intro file, but you will run the subsequent exercises by typing ".read [exercise file name]" into the "console" tab that is running sqlite."

You will not use the "Shell" tab at all during these exercises

To clear the console, type ".system clear" into the console.*/ 

--In SQL and other relational databases, a table is a collection of rows and columns. This concept is similar to spreadsheets and other data tables you may have seen.
--Each database is made up of many tables.

--This is an example of how to create a table and how we created the table on initial setup:

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

--Unlike Python, lines of code are not effected by changes in whitespace. Only a ';' will execute a statement and move on to the next step in SQL.

--Similar to what we've learned about variable types in Python, there are a number of different types in SQL. In SQL, the most common types are: 

--INT: An integer/whole number, positive or negative.
--VARCHAR(n): Similar to a string in python, it can be variable-length, and it will only store the characters needed.
--CHAR(n): Also similar to a string, but it can only store a fixed-length string. It can be faster than VARCHAR(n) if you know the exact length of the string you're storing. Often used for single-character codes.
--DATE: A date, stored in the format 'YYYY-MM-DD'.
--DECIMAL(n,m): A decimal number, with n digits before the decimal and m digits after the decimal.

--Additionally, the PRIMARY KEY designation, is use to create unique identifiers for each row/patient.

--Once you've created a table, you can insert data into it using the INSERT INTO command.

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

--You can also update data in a table using the UPDATE command.
UPDATE patients
SET first_name = 'Jim'
WHERE id = 7;

--However, be very specific with the records you update. If you don't specify which records you want to update, all records in the table will be updated. If 'id' is not specified, then all patients would have first_name updated to 'Jim'. 

--Additonally, you can delete data from a table using the DELETE command. This statement uses 'AND' to specify which records to delete. 
DELETE FROM patients
WHERE first_name = 'Michael' AND last_name = 'Brown';


--Here we create a second table with physician information. The INT PRIMARY KEY is used to ensure that each physician has a unique ID, and it we can use this ID to link the patients table to the physicians table, serving as the FOREIGN KEY for joining the two tables.

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
(103, 'Dr. Emma Brown', 'Pulmonology', 'Chicago', 'IL'),
(104, 'Dr. William Johnson', 'Neurology', 'Houston', 'TX'),
(105, 'Dr. Olivia Davis', 'Rheumatology', 'Phoenix', 'AZ'),
(106, 'Dr. Michael Wilson', 'Cardiology', 'San Francisco', 'CA'),
(107, 'Dr. Sophia Miller', 'Psychiatry', 'Seattle', 'WA'),
(108, 'Dr. James Taylor', 'Allergy and Immunology', 'Miami', 'FL'),
(109, 'Dr. Linda Anderson', 'Pain Management', 'Denver', 'CO'),
(110, 'Dr. Robert Thomas', 'Psychiatry', 'Boston', 'MA');

--To show the tables we've created, we can use the SELECT command.
SELECT * FROM patients;

--SQL can order items in a database with recognition and understanding of date formats
select * from patients order by date_of_birth;
select printf('');

--There are a number of different options that can be used to filter the data in a table. This example illustrates many ways we can narrow down our data when querying a large database:
SELECT * FROM patients
WHERE (first_name = 'James' OR first_name = 'John')
  AND last_name = 'Brown'
  AND date_of_birth BETWEEN '1930-01-01' AND '2000-12-31'
  AND primary_diagnosis IS NOT NULL
  AND primary_care_physician_id IN (101, 102, 103, 104, 105, 106, 107);

--To combine data from multiple tables, we can use the JOIN command. This command allows us to combine data from two tables based on a common field

--Here we are joining the patients table with the physicians table based on the physician_id field and summarizing the data with some columns removed

--These statements also show how to use the "AS" keyword to rename columns for the output. Labeling is particularly important when tables may have similarly named or ambiguous columns and we need to prevent confusion. 
--The statements "FROM patients p" and JOINT physicians ph" create aliases for each table. This technique is useful for .
    
SELECT 
    p.last_name AS patient_last_name,
    p.primary_diagnosis,
    p.primary_care_physician_id AS physician_id,
    ph.primary_specialty,
    ph.office_city
FROM 
    patients AS p
JOIN 
    physicians AS ph
ON 
    p.primary_care_physician_id = ph.physician_id;

--The primary_care_physician_id column in the patient table is the same as the physician_id column in the physicians table. We can use this to join the two tables and get the same output. This type of identifier is called a foreign key.

--Now, you can hit the green 'run' button at the top to initialize the database, and then move on to the next exercise: "2-crud.sql"


/* For learning beyond the scope of this tutorial and a deep dive into SQL, check out SQLZoo, a free resource with advanced SQL queries, additional concepts, and exercises built in to the browser. https://sqlzoo.net/wiki/SQL_Tutorial*/