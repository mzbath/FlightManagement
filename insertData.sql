-- ====================
-- 1. Insert data in 'City' table.
-- ====================
INSERT INTO City (cityID, cityName, country) VALUES
    (1, 'London', 'United Kingdom'),
    (2, 'Bristol', 'United Kingdom'),
    (3, 'Venice', 'Italy'),
    (4, 'Rome', 'Italy'),
    (5, 'Milan', 'Italy'),
    (6, 'Madrid', 'Spain'),
    (7, 'Barcelona', 'Spain'),
    (8, 'Paris', 'France'),
    (9, 'Berlin', 'Germany'),
    (10, 'Porto', 'Portugal'),
    (11, 'Zurich', 'Switzerland'),
    (12, 'Geneva', 'Switzerland'),
    (13, 'Budapest', 'Hungary'),
    (14, 'Athens', 'Greece'),
    (15, 'Amsterdam', 'The Netherlands');

-- ====================
-- 2. Insert data in 'Person' table.
-- ====================
INSERT INTO Person (personID, firstName, lastName, dateOfBirth, street, cityID, zip, email, phone, salary) VALUES
    (1, 'John', 'Doe', '1980-01-01', '123 Main St', 1, '11111', 'john1@example.com', '+44-111-1111', 40000),
    (2, 'Jane', 'Smith', '1990-02-02', '456 Oak Ave', 2, '22222', 'jane2@example.com', '+44-222-2222', 45000),
    (3, 'Alice', 'Johnson', '1985-03-03', '789 Pine Rd', 3, '33333', 'alice3@example.com', '+44-333-3333', 38000),
    (4, 'Bob', 'Brown', '1975-04-04', '10 Maple Ln', 4, '44444', 'bob4@example.com', '+44-444-4444', 37000),
    (5, 'Chris', 'Davis', '1988-05-05', '22 Cedar Dr', 5, '55555', 'chris5@example.com', '+44-555-5555', 42000),
    (6, 'Diana', 'Miller', '1992-06-06', '66 Elm St', 6, '66666', 'diana6@example.com', '+44-666-6666', 40000),
    (7, 'Evan', 'Wilson', '1981-07-07', '77 Birch Blvd', 7, '77777', 'evan7@example.com', '+44-777-7777', 52000),
    (8, 'Fiona', 'Moore', '1989-08-08', '88 Spruce Ct', 8, '88888', 'fiona8@example.com', '+44-888-8888', 39000),
    (9, 'George', 'Taylor', '1978-09-09', '99 Willow Way', 9, '99999', 'george9@example.com', '+44-999-9999', 31000),
    (10, 'Holly', 'Clark', '1991-10-10', '101 Lake Rd', 10, '10110', 'holly10@example.com', '+44-101-1010', 34000),
    (11, 'Ian', 'Adams', '1982-11-11', '110 Cherry Dr', 11, '11110', 'ian11@example.com', '+44-110-1111', 46000),
    (12, 'Jade', 'Baker', '1987-12-12', '120 Bay St', 12, '12120', 'jade12@example.com', '+44-120-1212', 43000),
    (13, 'Kyle', 'Wright', '1985-07-13', '130 River Pl', 13, '13130', 'kyle13@example.com', '+44-130-1313', 48000),
    (14, 'Lisa', 'Hall', '1993-02-14', '140 Forest Grv', 14, '14140', 'lisa14@example.com', '+44-140-1414', 45500),
    (15, 'Mark', 'Young', '1979-03-15', '150 Ocean Rd', 15, '15150', 'mark15@example.com', '+44-150-1515', 47000),
    (16, 'Marco', 'Rossi', '1993-09-15', '15 Paris Rd', 16, '16156', 'marco16@example.com', '+44-150-1616', 67000);

-- ====================
-- 3. Insert data in the 'FlightAttendant' table.
-- ====================
INSERT INTO FlightAttendant (personID, languageSpoken) VALUES
    (1, 'English'),
    (2, 'English'), (2, 'Spanish'),
    (3, 'French'), (3, 'English'),
    (6, 'English'), (6, 'Italian'), (6, 'French'),
    (8, 'German'), (8, 'English'), (8, 'Chinese'),
    (9, 'Dutch'), (9, 'English');

-- ====================
-- 4. Insert data in the 'Pilot' table.
-- ====================
INSERT INTO Pilot (personID, licenseNum, flightHours) VALUES
    (4, 'LC000', 400),
    (5, 'LIC001', 100),
    (7, 'LIC002', 220),
    (10, 'LIC003', 150),
    (11, 'LIC004', 800),
    (12, 'LIC005', 0),
    (13, 'LIC006', 340),
    (14, 'LIC007', 1000),
    (15, 'LIC008', 1200),
    (16, 'LIC009', 750);

-- ====================
-- 5. Insert data in the 'Crew' table.
-- ====================
INSERT INTO Crew (crewID) VALUES
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10),
(11),
(12),
(13),
(14),
(15),
(16),
(17),
(18),
(19),
(20);

-- ====================
-- 6. Insert data in the 'CrewFlightAttendant' table.
-- ====================
INSERT INTO CrewFlightAttendant (crewID, personID, role) VALUES
    (1, 1, 'Manager'),
    (2, 2, 'Attendant'),
    (3, 3, 'Attendant'),
    (4, 6, 'Manager'),
    (5, 8, 'Attendant'),
    (6, 9, 'Attendant'),
    (7, 1, 'Manager'),
    (8, 2, 'Attendant'),
    (9, 3, 'Attendant'),
    (10, 6, 'Manager'),
    (11, 8, 'Attendant'),
    (12, 9, 'Attendant'),
    (13, 1, 'Manager'),
    (14, 2, 'Attendant'),
    (15, 3, 'Attendant');

-- ====================
-- 7. Insert data in the 'CrewFlightAttendant' table.
-- ====================
INSERT INTO CrewPilot (crewID, personID, role) VALUES
    (1, 4, 'Pilot'),
    (1, 5, 'Copilot'),
    (2, 7, 'Pilot'),
    (2, 10, 'Copilot'),
    (3, 11, 'Copilot'),
    (3, 12, 'Pilot'),
    (4, 13, 'Pilot'),
    (4, 14, 'Copilot'),
    (5, 15, 'Copilot'),
    (5, 16, 'Pilot'),
    (6, 4, 'Copilot'),
    (6, 5, 'Pilot'),
    (7, 7, 'Pilot'),
    (8, 10, 'CoPilot'),
    (9, 16, 'Pilot'),
    (10, 12, 'Pilot'),
    (11, 13, 'Pilot'),
    (12, 14, 'Pilot'),
    (13, 15, 'Pilot'),
    (14, 16, 'Pilot'),
    (15, 4, 'Pilot');

-- ====================
-- 8. Insert data in the 'Airport' table.
-- ====================
INSERT INTO Airport (airportID, name, cityID) VALUES
    (1,  'Heathrow',  1),
    (2,  'La Guardia',  2),
    (3,  'Marco Polo',  3),
    (4,  'Fiumicino',  4),
    (5,  'Malpensa',  5),
    (6,  'Juan Carlos',  6),
    (7,  'Mar',  7),
    (8,  'Charles de Gaule',  8),
    (9,  'Marien Charles',  9),
    (10, 'Porto Alto', 10),
    (11, 'Platze', 11),
    (12, 'Mont Blanc', 12),
    (13, 'Sziget', 13),
    (14, 'Photos', 14),
    (15, 'Schripol', 15);

-- ====================
-- 9. Insert data in the 'Airplane' table.
-- ====================
INSERT INTO Airplane  (airplaneID, manufacturer, model, capacity, registrationNum) VALUES
    (1, 'Boeing', '737-800', 170, 'REG001'),
    (2, 'Airbus', 'A320', 180, 'REG002'),
    (3, 'Boeing', '777-300', 350, 'REG003'),
    (4, 'Airbus', 'A321', 200, 'REG004'),
    (5, 'Embraer', 'E190', 100, 'REG005'),
    (6, 'Boeing', '767-300', 220, 'REG006'),
    (7, 'Airbus', 'A350', 300, 'REG007'),
    (8, 'Boeing', '787-8', 242, 'REG008'),
    (9, 'Airbus', 'A220', 135, 'REG009'),
    (10, 'Boeing', '737 MAX', 178, 'REG010'),
    (11, 'Airbus', 'A330', 277, 'REG011'),
    (12, 'Boeing', '757-200', 200, 'REG012'),
    (13, 'Airbus', 'A340', 295, 'REG013'),
    (14, 'Comac', 'C919', 168, 'REG014'),
    (15, 'Boeing', '777-200', 305, 'REG015');


-- ====================
-- 10. Insert data in the 'Flights' table.
-- ====================
INSERT INTO Flight (flightID, date, depTime, arrTime, fromAirportID, toAirportID, airplaneID, crewID, status) VALUES
(1, '2025-01-01', '08:00', '10:00', 1, 2, 1, 1, 'Scheduled'),
(2, '2025-01-02', '09:00', '11:00', 2, 3, 2, 2, 'On time'),
(3, '2025-01-03', '07:30', '09:30', 3, 2, 3, 3, 'Delayed'),
(4, '2025-01-04', '12:00', '14:00', 4, 5, 4, 4, 'On time'),
(5, '2025-01-05', '06:00', '08:00', 5, 6, 5, 5, 'Scheduled'),
(6, '2025-01-06', '10:15', '12:15', 6, 4, 6, 6, 'On time'),
(7, '2025-01-07', '11:00', '13:00', 7, 4, 7, 7, 'Cancelled'),
(8, '2025-01-08', '14:30', '16:30', 8, 9, 8, 8, 'On time'),
(9, '2025-01-09', '09:45', '11:45', 9, 10, 9, 9, 'Scheduled'),
(10, '2025-01-15', '09:00', '11:00', 15, 1, 15, 10, NULL),
(11, '2025-01-16', '09:00', '11:00', 3, 1, 6, 11, NULL),
(12, '2025-01-16', '10:00', '13:00', 2, 1, 3, 12, NULL),
(13, '2025-01-16', '09:30', '11:30', 9, 1, 15, 13, NULL),
(14, '2025-01-14', '08:10', '10:10', 14, 15, 14, 14, 'Delayed'),
(15, '2025-01-20', '07:00', '09:00', 1, 3, 1, 16, 'Scheduled'),
(16, '2025-01-21', '08:30', '10:30', 2, 4, 2, 17, 'Scheduled'),
(17, '2025-01-22', '09:15', '11:15', 3, 5, 3, 18, 'Delayed'),
(18, '2025-01-23', '10:00', '12:00', 4, 6, 4, 19, 'On time');




