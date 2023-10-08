import pymysql;

# Establish database connection
db_connection = pymysql.connect(host="localhost",user="root",password="",database="smartcity_1")

# Create a cursor
cursor = db_connection.cursor()

# Functions to interact with streetlights

def add_streetlight(location):
    sql = "INSERT INTO streetlights (location, status) VALUES (%s, %s)"
    values = (location, 'OFF')
    cursor.execute(sql, values)
    db_connection.commit()
    print("Streetlight added successfully!")

def update_streetlight_status(id, status):
    sql = "UPDATE streetlights SET status = %s WHERE id = %s"
    values = (status, id)
    cursor.execute(sql, values)
    db_connection.commit()
    print("Streetlight status updated!")

def get_all_streetlights():
    sql = "SELECT * FROM streetlights"
    cursor.execute(sql)
    streetlights = cursor.fetchall()
    return streetlights

# Example usage

while True:
    print("\nSmart City Management System")
    print("1. Add Streetlight")
    print("2. Update Streetlight Status")
    print("3. View All Streetlights")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        location = input("Enter streetlight location: ")
        add_streetlight(location)
    elif choice == 2:
        streetlights = get_all_streetlights()
        for streetlight in streetlights:
            print(f"{streetlight[0]}. Location: {streetlight[1]}, Status: {streetlight[2]}")
        id = int(input("Enter streetlight ID to update: "))
        status = input("Enter new status (ON/OFF): ")
        update_streetlight_status(id, status)
    elif choice == 3:
        streetlights = get_all_streetlights()
        for streetlight in streetlights:
            print(f"ID: {streetlight[0]}, Location: {streetlight[1]}, Status: {streetlight[2]}")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")

# Close cursor and connection
cursor.close()
db_connection.close()
