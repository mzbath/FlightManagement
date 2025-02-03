# FlightManager
A Flight Management database-driven application developed using SQL and Python for Database and Cloud module at the MSc Computer Science, University of Bath (UK).

## Repository structure
This repo contains:
- A database ```airline.db```.
- The SQL queries to create the tables and add data: ```createTable.sql```, ```insertData.sql```.
- A python class to operate as database management system (DBMS) allowing interactions with the database: ```DBMS.py```.
- A python file to start the application: ```main.py```.
- A folder that includes all the SQL queries as defined in the assignment: ```sqlQueries/```.


## 1. Database setup in SQLite
The ```airline.db``` database is created and populated with the tables presented in ```createTable.sql``` file and these tables
are populated using the data included in ```insertData.sql``` file. 

These two ```.sql``` file are executed using python, from the ```main.py``` file.

Every time the ```main.py``` file is executed, if the tables in ```airlines.db``` are already present, these get deleted,
recreated, and populated with the data.

## 2. SQL queries and database interaction
The SQL queries used for flight retrival, schedule modification, pilot assignment, destination management, and data summary
are stored in ```sqlQueries/``` folder as separete files.

## 3. Application development in python (using SQLite3)
A class ```DBMS``` was created to act as a database management system. This class contains all the necessary methods/functions
to interact with the ```airline.db``` database.

The file ```main.py``` is the main file of the python application, where the ```DBMS``` is used.

## 4. How to run the application:
1. Open the ```main.py``` file.
2. Run the file using the arrow on the top right corner of VS code.
3. Interact with the app using the terminal.



