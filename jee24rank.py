# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:50:38 2025

@author: aditya namdeo
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Load Data
df_merged = pd.read_csv("df_merged.csv")

# Visualization Function
def visualize(Institute, Seat_Type, Gender):
    df_filtered = df_merged.loc[
        (df_merged["Institute"] == Institute) &  
        (df_merged["Seat Type"] == Seat_Type) & 
        (df_merged["Gender"] == Gender)
    ]
    
    if df_filtered.empty:
        st.error("No data available for the selected filters.")
        return

    fig, ax = plt.subplots(figsize=(20, 12))
    index = np.arange(len(df_filtered))
    width = 0.4
    x_labels = df_filtered["Academic Program Name"]
    ax.bar(index-width/2, df_filtered["Closing Rank"], width, label="Actual", alpha=0.7)
    ax.bar(index + width/2, df_filtered["Predicted Closing Rank 2024"], width, label="Predicted", alpha=0.7)
    ax.set_xlabel("Samples")
    ax.set_ylabel("Rank")
    ax.xticks(ticks=index, labels=x_labels, rotation=90, fontsize=10)
    ax.set_title("Actual vs Predicted Ranks")
    ax.legend()

    st.pyplot(fig)

# Streamlit UI
def main():
    st.title("JEE Advance 2024 Ranks Prediction Analyzer")

    institutes = df_merged["Institute"].unique()
    seat_type = df_merged["Seat Type"].unique()
    gender = df_merged["Gender"].unique()
    
    selected_institute = st.selectbox("Select an Institute", institutes)

    # Dynamically filter courses based on selected institute
    #filtered_courses = df_merged[df_merged["Institute"] == selected_institute]["Academic Program Name"].unique()
    #selected_course = st.selectbox("Select a Course", filtered_courses)

    selected_seat = st.selectbox("Select Seat Type", seat_type)
    selected_gender = st.selectbox("Select Gender", gender)

    if st.button("Show"):
        visualize(selected_institute, selected_seat, selected_gender)

if __name__ == "__main__":
    main()
