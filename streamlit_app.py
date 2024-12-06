import streamlit as st
import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

st.title("Linear Programming Solver")
method = st.sidebar.selectbox("Choose Method", ["Graphical", "Simplex", "Dual"])

st.subheader("Objective Function")
objective_type = st.radio("Objective", ["Maximize", "Minimize"])
coefficients = st.text_input("Enter coefficients of the objective function (comma-separated)", "2,3")
coefficients = np.array([float(c) for c in coefficients.split(',')])