import streamlit as st
import plotly.express as px
import pandas as pd

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")
data['DateTime'] = pd.to_datetime(data['DateTime'], format="%Y-%m-%d %H:%M:%S", errors='coerce')

# Sidebar
st.sidebar.title("Precious Metal Prices 2018-2021")
metal = st.sidebar.selectbox("Metal", data.columns[1:], index=1)
date_range = st.sidebar.date_input("Date Range", [data.DateTime.min().date(), data.DateTime.max().date()])

# Filter data
filtered_data = data.loc[(data.DateTime >= date_range[0]) & (data.DateTime <= date_range[1])]

# Create a plotly plot
fig = px.line(
    filtered_data,
    title="Precious Metal Prices 2018-2021",
    x="DateTime",
    y=[metal],
    color_discrete_map={
        "Platinum": "#E5E4E2",
        "Gold": "gold",
        "Silver": "silver",
        "Palladium": "#CED0DD",
        "Rhodium": "#E2E7E1",
        "Iridium": "#3D3C3A",
        "Ruthenium": "#C9CBC8"
    }
)

fig.update_layout(
    template="plotly_dark",
    xaxis_title="Date",
    yaxis_title="Price (USD/oz)",
    font=dict(
        family="Verdana, sans-serif",
        size=18,
        color="white"
    ),
)

# Streamlit app layout
st.title("Precious Metal Prices")
st.markdown("The cost of precious metals between 2018 and 2021")

# Display the plot
st.plotly_chart(fig, use_container_width=True)
