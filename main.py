from DBMS import DBMS

# Defining file names
DB_FILE = "airline.db" # database
DB_TABLES = "createTable.sql" # sql queries
DB_DATA = "insertData.sql" # sql queries

# Initialise the database management system
dbms = DBMS(DB_FILE)

# Clear the database from all the tables at the start of the application
dbms.drop_all_tables()

# Create tables in database
dbms.execute_sql_script(DB_TABLES)
# Add data to tables
dbms.execute_sql_script(DB_DATA)


# Run the application
print("Welcome to Flight Manager\n")
while True:
    print("\n Menu:")
    print("**********")
    print(" 1. View flights by criteria")
    print(" 2. Add a new flight")
    print(" 3. Update flight information")
    print(" 4. Assign pilot to flight")
    print(" 5. View pilot schedule")
    print(" 6. View/Update aiports information")
    print(" 7. Delete flight from database")
    print(" 8. Exit\n")

    try:
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            dbms.retrive_flight()
        elif __choose_menu == 2:
            dbms.add_new_flight()
        elif __choose_menu == 3:
            dbms.update_flight_info()
        elif __choose_menu == 4:
            dbms.assign_pilot_to_flight()
        elif __choose_menu == 5:
            dbms.retrive_pilot_schedule()
        elif __choose_menu == 6:
            dbms.view_and_update_airport_details()
        elif __choose_menu == 7:
            dbms.delete_flight_from_db()
        elif __choose_menu == 8:
            exit(0)
        else:
            print("Invalid Choice")

    # catch exception if the user does not enter an integer
    except ValueError:
        print("Invalide choice, retry.")
