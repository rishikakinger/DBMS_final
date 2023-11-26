import streamlit as st
from create import create_enter
from database import create_table_vehicleEnter
from read import read_no_vehicles


def main2():
    st.title("DRIVER DASHBOARD")
    menu2 = ["Vehicle ENTER", "Vehicle COUNT"]
    choice = st.sidebar.selectbox("Menu", menu2)

    
    if choice == "Vehicle ENTER":
        create_table_vehicleEnter()
        st.subheader("Enter Details:")
        create_enter()

    elif choice == "Vehicle COUNT":

        read_no_vehicles()

