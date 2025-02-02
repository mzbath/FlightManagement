import sqlite3

# =================================
# This class is used as the database management system (DBMS).
# It allows to create, read, update, and delete records from the database.
# =================================
class DBMS():

    def __init__(self, db: str):
        """ The db represents the .db file to be used. """
        self.db = db
        self.conn = None
        self.cur = None
#end-def


    def get_connection(self):
        """ This function is used to establish the connection with the database """

        if self.conn is None or self.cur is None:
            try: # create the connection is not available
                self.conn = sqlite3.connect(self.db)
                self.cur = self.conn.cursor()
            except Exception as e:
                print("Error connecting to the database: ", e)                  
#end-def

    def close_connection(self):
        """ Function to close the connection after the operations. """
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cur = None
#end-def

    def drop_all_tables(self):
        """
            Drops all tables from the SQLite database file used at instantiation of the class.
        """
        # ensure connection is active
        self.get_connection()
        try:
            # retrieve all table names from sqlite_master
            self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = self.cur.fetchall()

            # remove the tables if found
            if not tables:
                print("No tables found to be deleted.")
            else:
                for (table_name,) in tables:
                    self.cur.execute(f"DROP TABLE IF EXISTS {table_name};")
                self.conn.commit()

        # handle generic exceptions
        except Exception as ex:
            print("Error: tables could not be deleted,", ex)

        # ultimately close the connection
        finally:
            self.close_connection()
#end-def


    def execute_sql_script(self, filename: str):
        """
            This function is used to run the .sql files with the code necessary
            to create the tables in the database, and to insert data into those tables.
        """
    
        # ensure connection is active
        self.get_connection()
        
        # Read the sql script file
        with open(filename, "r") as file:
            sql_script = file.read()
        
        # Execute the SQL script
        self.cur.executescript(sql_script)
        
        # Commit changes and close connection
        self.conn.commit()
        self.close_connection()
#end-def



    def retrive_flight(self):
        """
            This function is used to retrive data from the 'Flight' table based on certain criteria.
            It works by appending conditions to WHERE in a sql query.
        """
        print("\nFlight search criteria:")
        origin = str(input("Enter flight origin (or leave it blank and press enter): "))
        destination = str(input("Enter flight destination (or leave it blank and press enter): "))
        status = str(input("Enter flight status (or leave it blank and press enter): "))
        from_date = str(input("Enter the start date (YYYY-MM-DD) of the flight/s you want to search (or leave it blank and press enter): "))
        to_date = str(input("Enter the end date (YYYY-MM-DD) of the flight/s you want to search (or leave it blank and press enter): "))

        # base query to which we will append conditions
        query = f"""
            SELECT f.flightID, f.date, f.depTime, f.arrTime, aFrom.name AS fromAirport, aTo.name AS toAirport, f.status   
            FROM Flight AS f
                JOIN Airport AS aFrom ON f.fromAirportID = aFrom.airportID
                JOIN Airport AS aTo ON f.toAirportID = aTo.airportID
            WHERE TRUE
                """
        # ensure connection is active
        self.get_connection()

        try: # addinf components to the query
            if origin:
                query += f" AND aFrom.name = '{origin}'"
            
            if destination:
                query += f" AND aTo.name = '{destination}'"

            if status:
                query += f" AND f.status = '{status}'"

            if from_date and to_date:
                query += f" AND f.date BETWEEN '{from_date}' AND '{to_date}'"
            elif from_date:
                query += f" AND f.date >= '{from_date}'"
            elif to_date:
                query += f" AND f.date <= '{to_date}'"

            # execute and fetch results of query
            self.cur.execute(query)
            results = self.cur.fetchall()

            if not results:
                print("\nNo flights found matching your criteria.")
                # flow control
                return

            # visualising results on terminal
            print("\n{:<9} {:<12} {:<10} {:<10} {:<20} {:<20} {:<12}".format("flightID", "Date", "depTime", "arrTime", "From", "To", "Status"))
            print("=" * 95)
            # print each row
            for row in results:
                flightID, date, depTime, arrTime, fromAirport, toAirport, status = row
                # handle None values
                depTime = depTime if depTime else "NA"
                arrTime = arrTime if arrTime else "NA"
                status = status if status else "NA"
                print(f"{flightID:<9} {date:<12} {depTime:<10} {arrTime:<10} {fromAirport:<20} {toAirport:<20} {status:<12}")

        except Exception as e:
            print("Error: query not successful: ", e)
#end-def

    
    def update_departure_time(self, flightID: int, newDepartureTime: str):
        """
            This function is used to update the departure time of a flight in the database.
            The sql query has been parameterised to prevent sql injections.
        """
        
        # ensure connection is active
        self.get_connection()

        try:
            # execute and commit the query
            self.cur.execute("UPDATE Flight SET depTime = ? WHERE flightID = ?", (newDepartureTime,flightID))
            self.conn.commit()

            # feedback to user
            print(f"Departure time for {flightID} updated to {newDepartureTime} !\n")
        
        except Exception as e:
            print("Error: update not completed: ", e)
#end-def


    def update_arrival_time(self, flightID: int, newArrivalTime: str):
        """
            This function is used to update the arrival time of a flight in the database.
            The sql query has been parameterised to prevent sql injections.
        """

        # ensure connection is active
        self.get_connection()

        try:
            # execute and commit the query
            self.cur.execute("UPDATE Flight SET arrTime = ? WHERE flightID = ?", (newArrivalTime, flightID))
            self.conn.commit()

            # feedback to user
            print(f"Arrival time for flight ID {flightID} successfully updated to {newArrivalTime} !\n")
        
        except Exception as e:
            print("Error: update not completed: ", e)
#end-def

        
    def update_flight_status(self, flightID: int, status: str):
        """
            This function is used to update the status of a flight in the database.
            The sql query has been parameterised to prevent sql injections.
        """

        # ensure connection is active
        self.get_connection()

        try:
            # execute and commit query
            self.cur.execute("UPDATE Flight SET status = ? WHERE flightID = ?", (status, flightID))
            self.conn.commit()

            # feedback to user
            print(f"Flight ID {flightID} status seccessfully updated to {status} !")
        
        except Exception as e:
            print("Error: update not completed: ", e)
#end-def

    def update_flight_departure_airport(self, flightID: int, depAirport: str):
        """
            This function is used to update the departure airport of a flight in the database.
            The sql query has been parameterised to prevent sql injections.
        """

        # ensure connection is active
        self.get_connection()

        try:
            # collect the airport id based on airport name
            self.cur.execute("SELECT airportID FROM Airport WHERE name = ?", (depAirport,)) # parameters are tuples
            airport_id = self.cur.fetchone()

            # handle invalid airport name
            if not airport_id:
                print(f"Error: no airport found with name '{depAirport}'.")
                return

            # extract airport id
            airport_id = airport_id[0]

            # update flight departure airport
            self.cur.execute("UPDATE Flight SET fromAirportID = ? WHERE flightID = ?", (airport_id, flightID))
            self.conn.commit()

            # feedback to user
            print(f"Departure airport for flight ID {flightID} updated to {depAirport} !\n")
        
        except Exception as e:
            print("Error: update not completed: ", e)
#end-def

    def update_flight_arrival_airport(self, flightID: int, arrAirport: str):
        """
            This function is used to update the arrival airport of a flight in the database.
            The sql query has been parameterised to prevent sql injections.
        """
        
        # ensure connection is active
        self.get_connection()

        try:
            # collect the airport id based on airport name
            self.cur.execute(f"""SELECT airportID FROM Airport WHERE name = '{arrAirport}'""")
            airport_id = self.cur.fetchone()

            # handle invalid airport name
            if not airport_id:
                print(f"Error: No airport found with name '{arrAirport}'.")
                # flow control
                return

            # extract airport id
            airport_id = airport_id[0]

            # update flight arrival airport
            self.cur.execute("UPDATE Flight SET fromAirportID = ? WHERE flightID = ?", (airport_id, flightID))
            self.conn.commit()

            # feedback to user
            print(f"Arrival airport for flight ID {flightID} updated to {arrAirport} !\n")
        
        except Exception as e:
            print("Error: update not completed: ", e)
#end-def

    def update_flight_info(self):
        """
            This function uses the previously defined functions to update flight records
            based on the input provided by the user.
        """

        # display available options to the user
        print("\nPlease choose from the following options:")
        print("1. Update flight departure time")
        print("2. Update flight arrival time")
        print("3. Update flight status")
        print("4. Update flight departure airport")
        print("5. Update flight arrival airport\n")

        # ensure connection is active
        self.get_connection()

        # menu
        __choose_menu = int(input("Enter your choice: "))
        # options
        if __choose_menu == 1:
            flightID = int(input("Enter the flight ID: "))
            newDepartureTime = str(input("Enter new departure time (HH:MM): "))
            self.update_departure_time(flightID, newDepartureTime)
        elif __choose_menu == 2:
            flightID = int(input("Enter the flight ID: "))
            newArrivalTime = str(input("Enter new arrival time (HH:MM): "))
            self.update_arrival_time(flightID, newArrivalTime)
        elif __choose_menu == 3:
            flightID = str(input("Enter flight ID: "))
            status = str(input("Enter the status of the flight: "))
            self.update_flight_status(flightID, status)
        elif __choose_menu == 4:
            flightID = str(input("Enter flight ID: "))
            depAirport = str(input("Enter the new departure airport: "))
            self.update_flight_departure_airport(flightID, depAirport)
        elif __choose_menu == 5:
            flightID = str(input("Enter flight ID: "))
            arrAirport = str(input("Enter the new arrival airport: "))
            self.update_flight_arrival_airport(flightID, arrAirport)

        # ultimately close connection with database
        self.close_connection()
#end-def


    def retrive_pilot_schedule(self):
        """
             This function is used to retrive the schedule of a pilot given his/her first
             and last name.
             The query used had to merge the tables 'Pilot' (to get the persons being pilots), 
             'Person' (to collect first and last name), 'CrewPilot' (to identify the crews involving the pilot),
             'Flight' (to collect flight info for those crews) [these are natural joins because they have common
             column names], 'Airport' (to get the name of destination and origin of flight) [these are specific
             inner joins using columns because the names are different].
        """
        # user input
        pilotFirstName = str(input("Enter pilot first name: "))
        pilotLastName = str(input("Enter pilot last name: "))
        full_name = pilotFirstName + " " + pilotLastName

        # string concatenation in sqlite syntax
        query = f"""
                SELECT firstName || ' ' || lastName AS pilotName, flightID, date, depTime, arrTime,
                    a1.name AS originAirport, a2.name AS destinationAirport, status
                FROM Pilot
                NATURAL JOIN Person
                NATURAL JOIN CrewPilot
                NATURAL JOIN Flight
                INNER JOIN Airport AS a1 ON fromAirportID = a1.airportID
                INNER JOIN Airport AS a2 ON toAirportID = a2.airportID
                WHERE firstName || ' ' || lastName = ?
                ORDER BY date, depTime;
                """
        
        # ensure connection is active
        self.get_connection()

        try: 
            # execute and fetch query results
            self.cur.execute(query, (full_name,))
            results = self.cur.fetchall()

            # handle invalid pilot name or empty schedule
            if not results:
                print(f"Error: no flight schedule found for pilot: {full_name}.")
                # flow control
                return
            
            # visualise results on terminal
            print("\n{:<20} {:<10} {:<12} {:<10} {:<10} {:<20} {:<20} {:<12}".format(
                "Pilot Name", "FlightID", "Date", "DepTime", "ArrTime", "From", "To", "Status"))
            print("=" * 120)
            # print each row
            for row in results:
                pilotName, flightID, date, depTime, arrTime, originAirport, destinationAirport, status = row
                # handle NULL values from database
                depTime = depTime if depTime else "NA"
                arrTime = arrTime if arrTime else "NA"
                status = status if status else "NA"
                print(f"{pilotName:<20} {flightID:<10} {date:<12} {depTime:<10} {arrTime:<10} {originAirport:<20} {destinationAirport:<20} {status:<12}")
    
        except Exception as e:
            print("Error: update not completed: ", e)

        finally:
            self.close_connection()
#end-def

    
#     def assign_pilot_to_flight(self):
#         """
#             This function allows to assign a given pilot to a flight by specifying the
#             flight ID.
#         """

#         # user input
#         flightID = int(input("Enter flight ID: "))
#         pilotFirstName = str(input("Enter pilot first name: "))
#         pilotLastName = str(input("Enter pilot last name: "))
        
#         # ensure connection is active
#         self.get_connection()

#         try:
#             # Check if the pilot exists
#             self.cur.execute("SELECT personID FROM (Pilot NATURAL JOIN Person) WHERE firstName = ? AND lastName = ?", (pilotFirstName, pilotLastName))
#             person_row = self.cur.fetchone()

#             # handle invalid pilot name
#             if not person_row:
#                 print(f"Error: pilot {pilotFirstName + " " + pilotLastName} does not exist.")
#                 # flow control
#                 return

#             # get the person id
#             pilot_id = person_row[0]

#             # check if the flight exists
#             self.cur.execute("SELECT crewID FROM Flight WHERE flightID = ?", (flightID,))
#             flight_row = self.cur.fetchone()

#             # handle invalid flight ID
#             if not flight_row:
#                 print(f"Error: Flight with ID {flightID} does not exist.")
#                 # flow control
#                 return

#             # get the crew ID assigned to this flight as it is the only column selected
#             crew_id = flight_row[0]  

#             # insert the pilot into the CrewPilot table
#             self.cur.execute("INSERT INTO CrewPilot (crewID, personID, role) VALUES (?, ?, 'Pilot')", (crew_id, pilot_id))
#             self.conn.commit()

#             # feedback to user
#             print(f"Pilot {pilotFirstName + " " + pilotLastName} successfully assigned to flight {flightID} as 'Pilot'.")
            
#         except Exception as e:
#             print("Error: pilot could not be assigned to flight: ", e)

#         finally:
#             self.close_connection()
# #end-def

    
    def view_all_airports(self):
        """
            This function allows to visualise on the terminal all the 
            available airports in the database.
        """

        # sql query to collect all the names of ariports and their location, city, country, hence the join
        query = "SELECT airportID, name AS airportName, cityName AS city, country FROM (Airport NATURAL JOIN City)"
        
        # ensure connection is active
        self.get_connection()

        try:
            # execute and fetch the results
            self.cur.execute(query)
            airports = self.cur.fetchall()

            # visualise data on terminal
            print("\n{:<11} {:<20} {:<15} {:<10}".format(
                "airportID", "AirportName", "City", "Country"))
            print("=" * 60)
            # print each row in a formatted way
            for airport in airports:
                airport_id, name, city, country = airport
                print(f"{airport_id:<11} {name:<20} {city:<15} {country}")
        
        except Exception as e:
            print("Error: airports data could not be visualised, ", e)
#end-def

    
    def update_airport_name(self, airportName: str, newAirportName: str):
        """
            This function allows to update the name of an airport given its original name
            and providing the new name to be used.
        """

        # ensure connection is active
        self.get_connection()

        try:
            # collect airport ID of the old airport name
            self.cur.execute("SELECT airportID from Airport WHERE name = ?", (airportName,))
            airport_row = self.cur.fetchone()

            # handle invalid old airport name
            if not airport_row:
                print(f"Error: no airport found with name '{airportName}'")
                # flow control
                return
            
            # collect old name airport id
            airportID = airport_row[0]
            # update the airport with the new name
            self.cur.execute("UPDATE Airport SET name = ? WHERE airportID = ?", (newAirportName,airportID))
            self.conn.commit()

            # feedback to user
            print(f"Airport {airportName} has been successfully renamed to {newAirportName} !")

        except Exception as e:
            print("Error: airport could not be renamed, ", e)
#end-def

    def add_new_airport(self, name: str, city: str, country: str):
        """
            This function allows to add a new aiport to the database by providing its name, city
            and country.
        """
        
        # ensure conncetion is active
        self.get_connection()

        try:
            # check if the city already exists so the same id needs to be used
            self.cur.execute("SELECT cityID FROM City WHERE cityName = ?", (city,))
            city_row = self.cur.fetchone()

            # if the city is not in the database it will be added
            if not city_row:
                self.cur.execute("SELECT MAX(cityID) FROM City")
                id_row = self.cur.fetchone()
                top_id = id_row[0] + 1
                self.cur.execute("INSERT INTO City (cityID, cityName, country) VALUES (?, ?, ?)", (top_id, city, country))
                self.conn.commit()
                cityID = self.cur.lastrowid
            # otherwise get the city id
            else:
                cityID = city_row[0]

            # addd new airport to database
            self.cur.execute("SELECT MAX(airportID) FROM Airport") # get the current max id in table
            airport_row = self.cur.fetchone() 
            top_airportID = airport_row[0] + 1 # create new id for the new airport
            self.cur.execute("INSERT INTO Airport (airportID, name, cityID) VALUES (?, ?, ?)", (top_airportID, name, cityID))
            self.conn.commit()

            # feedback to user
            print(f"Airport {name} ({city}, {country}) added to database !")

        except Exception as e:
            print("Error: adding the new airport to database, ", e)
#end-def


    def view_and_update_airport_details(self):
        """
            This function uses the previously defined functions to view the available
            airports, update the name of an airport, and add a new airport to the
            database.
        """
        # user input
        print("\nSelect one of the following options:")
        print("1. View the available airports")
        print("2. Update the name of an airport")
        print("3. Add a new airport to the database\n")

        # ensure connection is active
        self.get_connection()

        # menu
        __choose_menu = int(input("Enter your choice: "))
        # options
        if __choose_menu == 1:
            self.view_all_airports()
        elif __choose_menu == 2:
            airportName = str(input("Enter the airport name to be changed: "))
            newAirportName = str(input("Enter the new airport name: "))
            self.update_airport_name(airportName, newAirportName)
        elif __choose_menu == 3:
            name = str(input("Enter airport name: "))
            city = str(input("Enter the city where the airport is located: "))
            country = str(input("Enter the country where the airport is located: "))
            self.add_new_airport(name, city, country)

        # close connection
        self.close_connection()
#end-def

    
    def get_available_airplanes(self, date: str):
        """
            This function is used to find an available airplane for 
            a specified date.
        """
        # ensure conenction is open
        self.get_connection()

        try:
            # get available planes on the specified date
            query = """
                    SELECT airplaneID FROM Airplane
                    WHERE airplaneID NOT IN (SELECT DISTINCT airplaneID FROM Flight WHERE date = ?)
                    """
            self.cur.execute(query, (date,))
            available_airplanes = self.cur.fetchall()

            # handle unavailable airplanes
            if not available_airplanes:
                print(f"Error: no available airplanes on {date}.")
                return []

            # retunr the list of available airplanes
            return available_airplanes

        except Exception as e:
            print("Error: it was not possible to retrieve available airplanes, ", e)
            return []
#end-def

    def find_available_crew(self, date):
        """
            This function is used to get an available crew on the
            specified date.
        """
        # ensure connection is open
        self.get_connection()

        try:
            # get available crews on a specified date
            query = """
                    SELECT crewID FROM Crew
                    WHERE crewID NOT IN (SELECT crewID FROM Flight WHERE date = ?)
                    """
            self.cur.execute(query, (date,))    
            available_crews = self.cur.fetchall()

            # handle not available crews
            if not available_crews:
                print("Error: no available crew for that specific date.")
                return []

            return available_crews
        
        except Exception as e:
            print("Error: it was not possible to retrieve available crews, ", e)
            return []
#end-def 


    def add_new_flight(self):
        """
            This function allows to add a new flight to the database.
            Flight ID is generated automatically by getting the highest current id and add 1 to it.
            It ensures that a unique crew is created for the new flight.
            Airplane ID is assigned automatically by using the previous function and finding an 
            airplane that is free on that day.
        """

        # user input
        flight_date = str(input("Enter the flight date (YYYY-MM-DD): "))
        deptTime = str(input("Enter departure time (HH:MM): "))
        fromAirport = str(input("Enter the origin of the flight: "))
        toAirport = str(input("Enter the destination of the flight: "))

        # ensure connection is active
        self.get_connection()

        try:
            # find the id of departure airport
            self.cur.execute("SELECT airportID FROM Airport WHERE name = ?", (fromAirport,))
            deptAirportID_ = self.cur.fetchone()

            # handle invalid departure airport
            if not deptAirportID_:
                print(f"Error: departure airport '{fromAirport}' not found.")
                # flow control
                return
            
            # get departure airport id
            deptAirportID = deptAirportID_[0]

            # find id of the arrival airport
            self.cur.execute("SELECT airportID FROM Airport WHERE name = ?", (toAirport,))
            arrAirportID_ = self.cur.fetchone()

            # handle invalid arrival airport
            if not arrAirportID_:
                print(f"Error: departure airport '{fromAirport}' not found.")
                # flow control
                return
            

            # get arrival airport di
            arrAirportID = arrAirportID_[0]

            # it finds the current top flightID and creates the new one by adding one to the previous one
            self.cur.execute("SELECT MAX(flightID) FROM Flight")
            top_flight_id_ = self.cur.fetchone()
            newFlightID = int(top_flight_id_[0]) + 1 # casting flightID to integer to make sure it is integer

            # generate the new crewID
            self.cur.execute("SELECT MAX(crewID) FROM Crew")
            top_crew_id = self.cur.fetchone()[0] or 0
            newCrewID = int(top_crew_id) + 1
            # add the new crew id to the table
            self.cur.execute("INSERT INTO Crew (crewID) VALUES (?)", (newCrewID,))

            # find an available airplane for that date
            available_airplanes = self.get_available_airplanes(flight_date)
            # get the first available airplane
            available_airplane_ID = available_airplanes[0][0]

            # adding new flight to database
            query = """INSERT INTO Flight (flightID, date, depTime, arrTime, fromAirportID, toAirportID, airplaneID, crewID, status)
                       VALUES (?, ?, ?, NULL, ?, ?, ?, ?, NULL)
                    """
            self.cur.execute(query, (newFlightID,flight_date,deptTime,deptAirportID,arrAirportID,available_airplane_ID,newCrewID))
            self.conn.commit()

            # feedback to user
            print(f"Flight on date {flight_date}, time {deptTime}, departing from {fromAirport} and arriving to {toAirport} has been added to database !\n")
        
        except Exception as e:
            print("Error: the flight has not been created, ", e)
#end-def      

    def assign_pilot_to_flight(self):
        """
            This function allows to assign a certain pilot to a flight specified as
            flight ID.
        """

        # user input
        flightID = int(input("Enter flight ID: "))
        pilotFirstName = str(input("Enter pilot first name: "))
        pilotLastName = str(input("Enter pilot last name: "))

        # ensure connection is open
        self.get_connection()

        try:
            # check if the pilot exists
            self.cur.execute("SELECT personID FROM Pilot NATURAL JOIN Person WHERE firstName = ? AND lastName = ?", (pilotFirstName, pilotLastName))
            person_row = self.cur.fetchone()

            # handle invalid pilot name
            if not person_row:
                print(f"Error: pilot {pilotFirstName} {pilotLastName} not found in database.")
                # flow control
                return
            
            # get the pilot person id
            pilot_id = person_row[0]

            # check if the flight exists
            self.cur.execute("SELECT crewID FROM Flight WHERE flightID = ?", (flightID,))
            flight_row = self.cur.fetchone()

            # handle invalid flight id
            if not flight_row:
                print(f"Error: flight ID {flightID} not found in database.")
                # flow control
                return

            # get crew ID based on flight ID
            crew_id = flight_row[0]

            # assign the pilot to the crew
            self.cur.execute("INSERT INTO CrewPilot (crewID, personID, role) VALUES (?, ?, 'Pilot')", (crew_id, pilot_id))
            self.conn.commit()

            # feedback to user
            print(f"Pilot {pilotFirstName} {pilotLastName} assigned to flight ID {flightID} !")

        except Exception as e:
            print(f"Error: pilot could not be added to flight ID {flightID}, ", e)

        finally:
            self.close_connection()
#end-def

        
    def delete_flight_from_db(self):
        """
            This function allows to remove a record from the 'Flight' table based
            on flight ID.
        """
        # user input
        flightID = int(input("Enter flight ID to be removed: "))

        # ensure connection is active
        self.get_connection()

        try:
            # check if the flight id exists in database
            self.cur.execute("SELECT * FROM Flight where flightID = ?", (flightID,))
            flight_row = self.cur.fetchone()

            # handle invalid flight id
            if not flight_row:
                print(f"Error: flight ID {flightID} was not found in database.")
                return
            
            # delete flight from database based onn flight id
            self.cur.execute("DELETE FROM Flight WHERE flightID = ?", (flightID,))
            self.conn.commit()

            # feedback to user
            print(f"Flight ID {flightID} successfully deleted !")

        except Exception as e:
            print(f"Error: flight ID {flightID} could not be deleted, ", e)

        finally:
            self.close_connection()
#end-def
        

    