.system clear 
--clearing the console for our next exercise

--Now we'll learn how to sort and filter data in SQL. For the

--First complete this select statement to generate a table only showing physician name and state. Order that table by state. You with use the "ORDER BY" syntax referenced in the intro file to sort the output.

/*Statement here*/
select physician_name, office_state from physicians order by office_state;
.print "------------------------------------------------------"
.print
/*print statements for a border and better readability*/
  
--Now select a physician with a name starting with "Dr. W" and with an office city that starts with "G"

/*Statement here*/
select physician_name, office_city from physicians where physician_name like 'Dr. W%' and office_city like 'G%';
.print "------------------------------------------------------"
.print

--Now select all patients with birthday between (inclusive of) Jan 1, 1930 and Dec 31, 1980

/*Statement here*/
select * from patients
where date_of_birth between '1930-01-01' and '1980-12-31';

--Run the output with ".read 3-sortfilter.sql"
