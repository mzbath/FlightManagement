-- Pilot Assignment: Assign pilots to flights and retrieve information about pilot schedules.

-- Retrieve pilot schedule:
-- NATURAL JOIN are possible where the column names are equal between tables.
-- I used INNER JOIN by specifying the columns where the column names differed between tables.
SELECT firstName || ' ' || lastName AS pilotName, flightID, date, depTime, arrTime,
        a1.name AS originAirport, a2.name AS destinationAirport, status
FROM Pilot
NATURAL JOIN Person
NATURAL JOIN CrewPilot
NATURAL JOIN Flight
INNER JOIN Airport AS a1 ON fromAirportID = a1.airportID
INNER JOIN Airport AS a2 ON toAirportID = a2.airportID
WHERE firstName || ' ' || lastName = 'Marco Rossi'
ORDER BY date, depTime;


-- Assign pilot 'Marco Rossi' to flight ID 15
INSERT INTO CrewPilot (crewID, personID, role) VALUES (
    (SELECT crewID FROM Flight WHERE flightID = 15),
    (SELECT personID FROM Person NATURAL JOIN Pilot WHERE firstName = 'Marco' AND lastName = 'Rossi'),
    'Pilot'
);


-- check Marco Rossi's schedule again to visualise the change
SELECT firstName || ' ' || lastName AS pilotName, flightID, date, depTime, arrTime,
        a1.name AS originAirport, a2.name AS destinationAirport, status
FROM Pilot
NATURAL JOIN Person
NATURAL JOIN CrewPilot
NATURAL JOIN Flight
INNER JOIN Airport AS a1 ON fromAirportID = a1.airportID
INNER JOIN Airport AS a2 ON toAirportID = a2.airportID
WHERE  firstName || ' ' || lastName = 'Marco Rossi'
ORDER  BY date, depTime;
