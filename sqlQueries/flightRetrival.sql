-- Flight Retrieval: Retrieve flights based on multiple criteria, such as destination, status, or departure date.

SELECT f.flightID, f.date, f.depTime, f.arrTime, aFrom.name AS fromAirport, aTo.name AS toAirport, f.status   
FROM Flight AS f
INNER JOIN Airport AS aFrom ON f.fromAirportID = aFrom.airportID
INNER JOIN Airport AS aTo ON f.toAirportID = aTo.airportID
WHERE fromAirport = 'Marco Polo'
     AND f.status = 'Delayed'
     AND f.date = '2025-01-03';