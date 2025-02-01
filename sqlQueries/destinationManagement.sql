-- Destination Management: View and update destination information as required.

-- View all available airports
SELECT airportID, name AS airportName, cityName AS city, country 
FROM Airport NATURAL JOIN City;

-- Rename Athens airport from Photos to Venizelos
UPDATE Airport SET name = 'Venizelos' 
WHERE airportID = 14;