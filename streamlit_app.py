import streamlit as st

# Page configuration
st.set_page_config(page_title="Linear Programming Solver", layout="wide")

# Title
st.title("Linear Programming Solver")

# Input for the number of variables and constraints
num_variables = st.number_input("Количество переменных:", min_value=1, value=3, step=1, key="num_vars")
num_constraints = st.number_input("Количество ограничений:", min_value=1, value=3, step=1, key="num_constraints")

# Objective Function
st.subheader("Целевая функция:")
objective = []
for i in range(num_variables):
    coef = st.number_input(f"Коэффициент для x{i+1}", key=f"obj_coef_{i}")
    objective.append(coef)
objective_type = st.radio("Тип задачи:", ["min", "max"], horizontal=True, key="obj_type")

# Constraints
st.subheader("Ограничения:")
constraints = []
for i in range(num_constraints):
    cols = st.columns([1, 1, 1, 1, 1])
    constraint = []
    for j in range(num_variables):
        coef = cols[j].number_input(f"x{j+1} коэффициент (ограничение {i+1})", key=f"con_{i}_{j}")
        constraint.append(coef)
    inequality = cols[num_variables].selectbox("Знак:", ["≤", "≥", "="], key=f"ineq_{i}")
    rhs = cols[num_variables + 1].number_input(f"Правая часть (ограничение {i+1})", key=f"rhs_{i}")
    constraint.append(inequality)
    constraint.append(rhs)
    constraints.append(constraint)

# Non-negativity
st.write("x₁, x₂, ..., xₙ ≥ 0")

# Additional options
fraction_toggle = st.checkbox("В виде дробей", value=True, key="fraction_view")
solution_toggle = st.checkbox("С решением", value=True, key="solution_view")

# Method Selection
method = st.selectbox("Метод:", ["Базовый симплекс-метод", "Другой метод"], key="method_select")

# Buttons
cols = st.columns([1, 1, 1])
with cols[0]:
    if st.button("Очистить"):
        st.experimental_rerun()
with cols[1]:
    if st.button("Решить"):
        st.write("Решение будет отображено здесь.")
with cols[2]:
    if st.button("В двойственную"):
        st.write("Переключение на двойственную задачу.")

# Footer or solution area
st.divider()
st.write("Создано с использованием Streamlit.")
