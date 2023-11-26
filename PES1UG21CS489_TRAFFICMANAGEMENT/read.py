import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_ViewVehEnter,count_vehicles,show_vehicles,read_record_count,officer_not, Citizen_not



def readvehicles():
    result=view_ViewVehEnter()
    df=pd.DataFrame(result,columns=['Date','Type','OwnerType','VehicleNumber','RoadID','ID','Name','Contact'])
    with st.expander("View all vehicle details"):
        st.dataframe(df)

def read_no_vehicles():
    result=count_vehicles()
    df=pd.DataFrame(result,columns=['Vehicle Count'])
    with st.expander("All the vehicles"):
        st.dataframe(df)

def read_Roads():
    result=show_vehicles()
    df=pd.DataFrame(result,columns=['Road ID','Status'])
    with st.expander("Status of the Roads"):
        st.dataframe(df)


def read_records_count():
    result=read_record_count()
    df=pd.DataFrame(result,columns=['Total records','Owner Type','Date'])
    with st.expander("Number of records per officer and citizen"):
        st.dataframe(df)

def read_notP():
    result=officer_not()
    df=pd.DataFrame(result,columns=['Contact','ID','Name'])
    with st.expander("Officers that are absent from duty"):
        st.dataframe(df)

def read_notC():
    result=Citizen_not()
    df=pd.DataFrame(result,columns=['Contact','ID','Name','No of cars'])
    with st.expander("Citizens driving"):
        st.dataframe(df)
