import streamlit as st
import pandas as pd

# Atur layout ke full layar
st.set_page_config(layout="wide")

st.title("ADM PLAN Viewer - Demo")

# Data contoh (dummy) supaya app bisa jalan tanpa file Excel
data = {
    "PO NO": ["Q4IC55HA", "Q4IC55HB", "Q4IC55HC"],
    "PART NO": ["81110BZ610", "81150BZ111", "81550BZ190"],
    "DELIVERY QUANTITY": [12, 8, 20],
}
df = pd.DataFrame(data)

# Tampilkan tabel
st.dataframe(df, use_container_width=True)
