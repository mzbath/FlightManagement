-- Queries that summarise data, such as the number of flights to each destination or the number of flights assigned to a pilot

-- Average salary of pilots and flight hours
SELECT AVG(salary) AS PilotAverageSalary, AVG(flightHours) AS PilotAverageFlightHours
FROM Pilot NATURAL JOIN Person;


-- Getting the number of flights for each pilot in the month of January 2025
SELECT personID, firstName || ' ' || lastName AS PilotName, COUNT(DISTINCT flightID) AS TotalFlights
FROM Pilot NATURAL JOIN Person NATURAL JOIN CrewPilot NATURAL JOIN Flight
GROUP BY personID
HAVING date BETWEEN '2025-01-01' AND '2025-01-31';


-- Getting the number of flights departing from and arriving to each airport
SELECT name AS AirportName, Arrivals, Departures, Arrivals+Departures AS TotalFlights 
FROM (SELECT toAirportID AS airportID, COUNT(toAirportID) AS Arrivals FROM Flight GROUP BY toAirportID)
NATURAL JOIN (SELECT fromAirportID as airportID, COUNT(fromAirportID) AS Departures FROM Flight GROUP BY fromAirportID)
NATURAL JOIN Airport
ORDER BY TotalFlights DESC;
-- the airports with more flights incoming and outgoing are Heathrow and La Guardia.