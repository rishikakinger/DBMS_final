import streamlit as st
from database import add_data_enter,add_data_citizen,add_data_Officer,remove_data_Road,remove_data_citizen,remove_data_Officer,add_data_Road

def create_enter():


    Enter_date = st.date_input("Date:")
    Veh_type= st.selectbox("Type:",["Two wheeler","Four wheeler"])
    Owner_type = st.selectbox("Owner Type:",["Officer","Citizen"])
    Veh_No = st.text_input("Vehicle_no:")
    road_id = st.text_input("Road_id:")
    id = st.text_input("ID:")


    if st.button("Add Vehicle"):
        add_data_enter(Enter_date, Veh_type, Owner_type, Veh_No, road_id,id)
        st.success(" Successfully added Vehicle record: {}".format(Veh_No))
    


def create_AddCitizen():

    Contact = st.text_input("Contact:")
    ID = st.text_input("ID:")
    Name = st.text_input("Name")
    no_of_cars = st.text_input("Number of vehicles")
    if st.button("Add Citizen"):
        add_data_citizen(Contact,ID, Name, no_of_cars)
        st.success(" Successfully added Citizen record: {}".format(ID))

def create_RemoveCitizen():

    ID= st.text_input("ID:")
    if st.button("Remove Citizen"):
        remove_data_citizen(ID)
        st.success(" Successfully Removed Citizen record: {}".format(ID))

def create_AddOfficer():
    Contact = st.text_input("Contact:")
    ID= st.text_input("ID:")
    Name = st.text_input("Name")
        
    if st.button("Add Police officer"):
        add_data_Officer(Contact, ID, Name)
        st.success(" Successfully added Police Officer record: {}".format(ID))

def create_RemoveOfficer():

        
    ID= st.text_input("ID:")
        
    if st.button("Remove Officer"):
        remove_data_Officer(ID)
        st.success(" Successfully removed Police officer record: {}".format(ID))


    

def create_AddRoad():

    road_id = st.text_input("Road ID:")
    Status= st.selectbox( "Status",("Active","Occupied"))
        
    if st.button("Add Road"):
        add_data_Road(road_id, Status)
        st.success(" Successfully added Road: {}".format(road_id))

def create_RemoveRoad():

    road_id = st.text_input("Road ID:")
        
    if st.button("Remove Road"):
        remove_data_Road(road_id)
        st.success(" Successfully removed Road: {}".format(road_id))


