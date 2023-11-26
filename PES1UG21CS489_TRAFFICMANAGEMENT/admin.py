import streamlit as st
from read import readvehicles,read_Roads,read_records_count,read_notP,read_notC
from create import create_AddRoad,create_AddCitizen,create_AddOfficer,create_RemoveOfficer,create_RemoveCitizen,create_RemoveOfficer,create_RemoveRoad
from database import create_table_Road,create_table_Citizen,create_table_Officer


def main1():
    st.title("TRAFFIC ADMIN")
    menu = ["Add Citizen Data", "Remove Citizen Data","Add Police Officer","Remove Police Officer","View Vehicles Entered","Add Road","Remove Road","Show Roads","Number of roads occupied","No police","No citizens"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table_Citizen()
    create_table_Officer()
    create_table_Road()

    if choice == "Add Citizen Data":
        st.subheader("Enter Details To Be Added:")
        create_AddCitizen()

    
    elif choice=="Remove Citizen Data":
        st.subheader("Enter Details To Be Removed:")
        create_RemoveCitizen()
    
    elif choice=="Add Police Officer":
        st.subheader("Enter Details To Be Added:")
        create_AddOfficer()

    
    elif choice=="Remove Police Officer":
        st.subheader("Enter Details To Be Removed:")
        create_RemoveOfficer()

    
    elif choice=="View Vehicles Entered":
        st.subheader("Vehices_Entered:")
        readvehicles()

    
    elif choice=="Add Road":
        st.subheader("Enter Details To Be Added:")
        create_AddRoad()

    
    elif choice=="Remove Road":
        st.subheader("Enter Details To Be Removed:")
        create_RemoveRoad()

    elif choice=="Show Roads":
        st.subheader("All Roads:")
        read_Roads()
        

    elif choice=="Number of roads occupied":
        st.subheader("Number of roads occupied by citizens and police officers:")
        read_records_count()

    elif choice=="No police":
        st.subheader("Not supervised by Police:")
        read_notP()

    elif choice=="No citizens":
        st.subheader("Not occupied by Citizens:")
        read_notC()

