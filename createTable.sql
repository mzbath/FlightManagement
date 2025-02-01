
-- CREATING TABLES: This script is used to create the tables from the relational schema

-- =======================
-- 1. Creating the 'Person' table.
-- phone is represented by a VARCHAR because it may include a + at the start and spaces.
-- salary was set to NUMERIC which can be represented as both an integer and a real data type (https://www.sqlite.org/datatype3.html).
-- =======================
CREATE TABLE Person (
    personID INTEGER NOT NULL,
    firstName VARCHAR(30) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    dateOfBirth DATE NOT NULL,
    street VARCHAR(50) NOT NULL,
    cityID INTEGER NOT NULL,
    zip VARCHAR(10) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    salary NUMERIC NOT NULL,
    PRIMARY KEY (personID),
    FOREIGN KEY (cityID) REFERENCES City(cityID) ON DELETE RESTRICT
);

-- =======================
-- 2. Creating the 'FlightAttendant' table which is a subtype of 'Person'.
-- languageSpoken was set to not null because every flight attendants speaks at least one language.
-- cascade is used so that if a person is deleted, their flight attendant should also be deleted.
-- =======================
CREATE TABLE FlightAttendant (
    personID INTEGER NOT NULL,
    languageSpoken VARCHAR(100) NOT NULL,
    PRIMARY KEY (personID, languageSpoken),
    FOREIGN KEY (personID) REFERENCES Person(personID) ON DELETE CASCADE
);

-- =======================
-- 3. Creating the 'Pilot' table which is a subtype of 'Person'.
-- flightHours may be null if a pilot has not flown yet.
-- licenseNum cannot be null as this person is a pilot.
-- CASCADE is used so that if a person is deleted, their pilot should also be deleted. 
-- =======================
CREATE TABLE Pilot (
    personID INTEGER NOT NULL,
    licenseNum VARCHAR(50) NOT NULL,
    flightHours INTEGER,
    PRIMARY KEY (personID),
    FOREIGN KEY (personID) REFERENCES Person(personID) ON DELETE CASCADE
);

-- =======================
-- 4. Creating the 'Crew' table
-- =======================
CREATE TABLE Crew (
    crewID  INTEGER NOT NULL,
    PRIMARY KEY (crewID)
);

-- =================================================
-- 5. CrewFlightAttendant (many-to-many relationship between Crew and FlightAttendant).
-- The primary key is composed by crewID and personID.
-- role represents the role of the flight attendant, for instance manager or crew, and it cannot be null.
-- =================================================
CREATE TABLE CrewFlightAttendant (
    crewID INTEGER NOT NULL,
    personID INTEGER NOT NULL,
    role VARCHAR(30) NOT NULL,
    PRIMARY KEY (crewID, personID),
    FOREIGN KEY (crewID) REFERENCES Crew(crewID) ON DELETE RESTRICT,
    FOREIGN KEY (personID) REFERENCES FlightAttendant(personID) ON DELETE RESTRICT
);

-- ================================================
-- 6. CrewPilot (many-to-many relationship between Crew and Pilot).
-- The primary key is composesd by crewID and personID.
-- role represents the role of the pilot, that is either pilot or copilot, and it cannot be null.
-- ================================================
CREATE TABLE CrewPilot (
    crewID INTEGER NOT NULL,
    personID INTEGER NOT NULL,
    role VARCHAR(30) NOT NULL,
    PRIMARY KEY (crewID, personID),
    FOREIGN KEY (crewID) REFERENCES Crew(crewID) ON DELETE RESTRICT,
    FOREIGN KEY (personID) REFERENCES Pilot(personID) ON DELETE RESTRICT
);

-- =======================
-- 7. Create the 'Airport' table.
-- all its atrtibutes cannot be null.
-- =======================
CREATE TABLE Airport (
    airportID INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    cityID INTEGER NOT NULL,
    PRIMARY KEY (airportID),
    FOREIGN KEY (cityID) REFERENCES City(cityID) ON DELETE RESTRICT      
);

-- =======================
-- 8. Create the 'Airplane' table.
-- All attributes contain important information and hence cannot be null.
-- registrationNum is a varchar because it may be an alphanumeric value.
-- =======================
CREATE TABLE Airplane (
    airplaneID INTEGER NOT NULL,
    manufacturer VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    capacity INTEGER NOT NULL,
    registrationNum VARCHAR(50) NOT NULL,
    PRIMARY KEY (airplaneID)        
);

-- =======================
-- 9. Create the 'City' table.
-- This table ensures 3rd normal form
-- =======================
CREATE TABLE City (
    cityID INTEGER NOT NULL,
    cityName VARCHAR(30) NOT NULL,
    country VARCHAR(30) NOT NULL,
    PRIMARY KEY (cityID)
);

-- =======================
-- 10. Create the 'Flight' table.
-- status needs to be a value in the provided list or null, as it was assumed that uncertainty on certain 
-- flights may lead to null values for status. However, values outside the list are not allowed.
-- arrTime can be null as it may not be defined yet, especially in case of delay.
-- =======================
CREATE TABLE Flight (
    flightID INTEGER NOT NULL,
    date DATE NOT NULL,
    depTime TIME NOT NULL,
    arrTime TIME,
    fromAirportID INTEGER NOT NULL,
    toAirportID INTEGER NOT NULL,
    airplaneID INTEGER NOT NULL,
    crewID INTEGER NOT NULL,
    status VARCHAR(20) CHECK(Status IN ('On time', 'Scheduled', 'Delayed', 'Cancelled', 'Departed', 'Arrived')),
    PRIMARY KEY (flightID),
    FOREIGN KEY (fromAirportID) REFERENCES Airport(airportID) ON DELETE RESTRICT,
    FOREIGN KEY (toAirportID) REFERENCES Airport(airportID) ON DELETE RESTRICT,
    FOREIGN KEY (airplaneID) REFERENCES Airplane(airplaneID) ON DELETE RESTRICT,
    FOREIGN KEY (crewID) REFERENCES Crew(crewID) ON DELETE RESTRICT 
);
