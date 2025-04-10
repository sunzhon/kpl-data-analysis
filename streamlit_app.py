# How to use the code
# Install dependencies: pip install pandas streamlit pygwalker
# Save as .py file
# Run with streamlit run your_filename.py


import pandas as pd
import numpy as np
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer

#uploaded_file = st.file_uploader("Your data file")
uploaded_file = "/home/admin-1/workspace/kepler_ws/KeplerRobot/logs/st_rl/k1_flat/2025-04-08_15-12-21/metrics/states_1.csv"
if uploaded_file is not None:
    all_df_data = pd.read_csv(uploaded_file)
    columns = list(all_df_data.columns)
    data_len=all_df_data.shape[0]
    rate=50

    all_df_data[r"time [s]"] = np.linspace(0,data_len/rate,data_len)
    rename_map={}
    for key in columns:
        if "tau" in key:
            rename_map[key]=f"{key} [Nm]"
        if "vel" in key:
            rename_map[key]=f"{key} [rad/s]"
        if "pos" in key:
            rename_map[key]=f"{key} [rad]"
        if "grf" in key:
            rename_map[key]=f"{key} [N]"
        if "command" in key:
            rename_map[key] = f"{key} [m/s]"
    
    all_df_data.rename(columns=rename_map,inplace=True)
    #df = pd.read_csv(uploaded_file)
    pyg_app = StreamlitRenderer(all_df_data)
    pyg_app.explorer()
