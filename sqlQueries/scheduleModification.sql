-- Schedule Modification: Update flight schedules (e.g., change departure time or status).

-- visualise all the records
SELECT * FROM Flight;
-- update the status of a flight
UPDATE Flight SET status = 'Delayed' WHERE flightID = 15;
-- update the departure time of a flight
UPDATE Flight SET depTime = '06:10' WHERE flightID = 18;
-- visualise change of record
SELECT * FROM Flight;