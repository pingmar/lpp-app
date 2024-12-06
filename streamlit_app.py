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

st.subheader("Constraints")
num_constraints = st.number_input("Number of constraints", min_value=1, value=2, step=1)
constraints = []
for i in range(num_constraints):
    constraint = st.text_input(f"Constraint {i+1} (format: 'a1,a2,... <= b')", "1,2 <= 10")
    constraints.append(constraint)

A, b = [], []
for constraint in constraints:
    parts = constraint.split("<=")
    A.append([float(x) for x in parts[0].split(',')])
    b.append(float(parts[1]))
A = np.array(A)
b = np.array(b)

if st.button("Solve"):
    if method == "Graphical":
        # Implement graphical solution (for two variables)
        if len(coefficients) != 2:
            st.error("Graphical method only supports 2 variables.")
        else:
            st.write("Solution via Graphical Method:")
            # Visualization
            fig, ax = plt.subplots()
            x = np.linspace(0, max(b), 400)
            for i, row in enumerate(A):
                ax.plot(x, (b[i] - row[0]*x)/row[1], label=f"Constraint {i+1}")
            ax.fill_between(x, 0, b[0] / A[0, 1], color='gray', alpha=0.3)
            ax.legend()
            st.pyplot(fig)

    elif method == "Simplex":
        st.write("Solution via Simplex Method:")
        res = linprog(c=-coefficients if objective_type == "Maximize" else coefficients, 
                      A_ub=A, b_ub=b, method="highs")
        st.write(f"Optimal value: {res.fun}, Variables: {res.x}")

    elif method == "Dual":
        st.write("Solution via Dual Problem:")
        # Transform to dual and solve
        dual_A = -A.T
        dual_b = -coefficients
        dual_c = b
        res_dual = linprog(c=dual_c, A_ub=dual_A, b_ub=dual_b, method="highs")
        st.write(f"Dual optimal value: {res_dual.fun}, Variables: {res_dual.x}")