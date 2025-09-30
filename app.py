import streamlit as st
import pandas as pd

# Atur layout ke full layar
st.set_page_config(layout="wide")

st.title("ADM PLAN Viewer")

# Coba baca file Excel
try:
    # Ganti dengan nama file yang kamu upload di repo
    file_path = "Master Picking List.xlsm"

    # Baca sheet "ADM PLAN"
    df = pd.read_excel(file_path, sheet_name="ADM PLAN")

    # Bersihkan baris/kolom kosong
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")

    # Tampilkan tabel
    st.dataframe(df, use_container_width=True)

except FileNotFoundError:
    st.error("⚠️ File 'Master Picking List.xlsm' belum ada di repository. Silakan upload dulu ke GitHub.")
