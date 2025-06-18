import streamlit as st
import numpy as np


st.set_page_config(
    page_title="IMPACT",
    page_icon="⚕️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("Immuno Nutritional Performance Assesment Combined Test")

with st.container(border=True):
    ecog = st.selectbox("ECOG:", ("0-1", "2-3-4"), index=None, key="ecog")
    monocyte = st.number_input(
        label="Monocyte (mm\u00b3)",
        step=0.01,
        value=0.00,
        format="%0.2f",
        key="monocyte",
    )

    albumin = st.number_input(
        label="Albumin (g/dl)", step=0.01, value=0.00, format="%0.2f", key="albumin"
    )


    score = 0
    if ecog == "2-3-4":
        score += 1

    calc = np.subtract(
        np.multiply(np.float128(albumin), np.float128(0.9)),
        np.multiply(np.float128(monocyte), np.float128(0.0007)),
    )
    if calc < 3.3:
        score += 1

    _, center_col, _ = st.columns([1, 1, 1])
    with center_col:
        calc_bt = st.button("Calculate Risk")

    if calc_bt:
        if ecog is None or monocyte is None or albumin is None:
            st.warning("Please fill all fields.")
        else:
            if score < 1:
                st.success(":green[Low risk]")
            elif score == 1:
                st.warning(":orange[Intermediate Risk]")
            elif score > 1:
                st.error(":red[High Risk]")
