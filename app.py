import streamlit as st
import datetime
import requests
import pandas as pd

'''
# TaxiFareModel front
'''

pickup_date = st.sidebar.date_input("When is the pickup?", datetime.date(2014, 7, 6))
pickup_time = st.sidebar.time_input("What time?", datetime.time(19, 18))

pickup_datetime = f"{pickup_date} {pickup_time}"

st.write(f"You pickup is set at {pickup_datetime}.")

pickup_latitude = st.sidebar.text_input("Pickup Latitude", "40.783282")
pickup_longitude = st.sidebar.text_input("Pickup Longitude", "-73.950655")

dropff_latitude = st.sidebar.text_input("Dropoff Latitude", "40.769802")
dropff_longitude  = st.sidebar.text_input("Dropoff Longitude", "-73.984365")

passenger_count = st.sidebar.text_input("Passenger Count", "2")

st.write(f"You start from {pickup_latitude}, {pickup_longitude}.")

# location = {}
# if not location:
#     st.write("Waiting for location...")
#     location = streamlit_geolocation()
# else:
#     st.write("Your location is:", location.latitude, location.longitude)

# data = {
#     'lat': dropff_latitude,
#     'lon': dropff_longitude
# }
# df = pd.DataFrame(data)

# st.map(df, latitude=dropff_latitude, longitude=dropff_longitude, size=100, color='red', zoom=100)


url = 'https://taxifare.lewagon.ai/predict'

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropff_longitude,
    "dropoff_latitude": dropff_latitude,
    "passenger_count": passenger_count
}

response = requests.get(url, params=params)

json_response = response.json()

prediction = json_response.get('fare')

st.write("Ca va te couter :", prediction)
