
import mysql.connector 


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2393",
    database="dbmsfinal"
)
c = mydb.cursor()

def create_table_vehicleEnter():
    c.execute('CREATE TABLE IF NOT EXISTS Vehicle_in(Date DATE, Type TEXT, Owner_type TEXT, Vehicle_no varchar(50), P_id varchar(2),ID varchar(13))')
    mydb.commit()

def add_data_enter(Date, Type,Owner_type, Vehicle_no, road_id,id):
    c.execute('INSERT INTO Vehicle_in(Date, Type, Owner_type,Vehicle_no, P_id,ID) VALUES (%s,%s,%s,%s,%s,%s)',
              (Date, Type,Owner_type, Vehicle_no, road_id,id))
    c.execute('CALL StatusUpdation("{}")'.format(road_id))
    mydb.commit()


def count_vehicles():
    c.execute('SELECT COUNT(P_id) from Vehicle_in')
    data=c.fetchall()
    mydb.commit()
    return data
    

def create_table_Citizen():
    c.execute('CREATE TABLE IF NOT EXISTS citizen(Contact varchar(10), ID varchar(13), Name varchar(50), no_of_cars INT)')
    mydb.commit()

def create_table_Officer():
    c.execute('CREATE TABLE IF NOT EXISTS officer(Contact varchar(10), ID varchar(13), Name varchar(50))')
    mydb.commit()

def create_table_Road():
    c.execute('CREATE TABLE IF NOT EXISTS road(road_id varchar(2), Status TEXT)')
    mydb.commit()


def add_data_citizen(contact,ID,Name,no_of_cars):
    c.execute('INSERT INTO citizen(Contact, ID , Name , no_of_cars) VALUES (%s,%s,%s,%s)',(contact,ID,Name,no_of_cars))
    mydb.commit()

def remove_data_citizen(ID):
    c.execute('DELETE FROM citizen WHERE ID="{}"'.format(ID))
    mydb.commit()

def add_data_Officer(Contact,ID,Name):
    c.execute('INSERT INTO officer(Contact , ID , Name ) VALUES (%s,%s,%s)',(Contact,ID,Name))
    mydb.commit()

def remove_data_Officer(ID):
    c.execute('DELETE FROM officer WHERE ID="{}"'.format(ID))
    mydb.commit()

def add_data_Road(road_id,Status):
    c.execute('INSERT INTO road(road_id , Status) VALUES (%s,%s)',(road_id,Status))
    mydb.commit()

def remove_data_Road(road_id):
    c.execute('DELETE FROM road WHERE road_id="{}"'.format(road_id))
    mydb.commit()

def view_ViewVehEnter():
    c.execute("SELECT Vehicle_in.Date, Vehicle_in.Type, Vehicle_in.Owner_type AS OwnerType, Vehicle_in.Vehicle_no AS VehicleNumber, Vehicle_in.P_id AS RoadID, Vehicle_in.ID, COALESCE(officer.Name, citizen.Name) AS Name, COALESCE(officer.Contact, citizen.Contact) AS Contact FROM Vehicle_in LEFT JOIN officer ON Vehicle_in.Owner_type = 'Officer' AND Vehicle_in.ID = officer.ID LEFT JOIN citizen ON Vehicle_in.Owner_type = 'Citizen' AND Vehicle_in.ID = citizen.ID;")
    data = c.fetchall()
    return data

def show_vehicles():
    c.execute('SELECT * FROM road')
    data=c.fetchall()
    return data


def read_record_count():
    c.execute('SELECT count(*) as total_records,Owner_type,Date  FROM Vehicle_in group by date,Owner_type;')
    data=c.fetchall()
    return data    

def officer_not():
    c.execute('SELECT * FROM officer WHERE officer.ID NOT IN ( SELECT ID FROM Vehicle_in);')
    data=c.fetchall()
    return data

def Citizen_not():
    c.execute('Select * from citizen where citizen.ID NOT IN(Select ID from Vehicle_in);')
    data=c.fetchall()
    return data