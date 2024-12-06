import streamlit as st

# Title
st.title("Linear Programming Solver")

# Inputs for the number of variables and constraints
num_variables = st.number_input("Количество переменных:", min_value=1, value=3, step=1)
num_constraints = st.number_input("Количество ограничений:", min_value=1, value=3, step=1)

st.write("### Целевая функция:")
# Inputs for the coefficients of the objective function
objective_function = []
for i in range(num_variables):
    coef = st.number_input(f"Коэффициент для x{i+1}:", key=f"objective_{i}")
    objective_function.append(coef)
objective_type = st.selectbox("Тип:", ["min", "max"], key="objective_type")

st.write("### Ограничения:")
# Inputs for constraints
constraints = []
for i in range(num_constraints):
    st.write(f"Ограничение {i+1}:")
    constraint = []
    for j in range(num_variables):
        coef = st.number_input(f"Коэффициент для x{j+1} в ограничении {i+1}:", key=f"constraint_{i}_{j}")
        constraint.append(coef)
    rhs = st.number_input(f"Правая часть для ограничения {i+1}:", key=f"rhs_{i}")
    sign = st.selectbox(f"Знак ограничения {i+1}:", ["<=", "=", ">="], key=f"sign_{i}")
    constraints.append((constraint, rhs, sign))

st.write("x₁, x₂, ..., xₙ ≥ 0")

# Toggle options
fraction_view = st.checkbox("В виде дробей")
show_solution = st.checkbox("С решением")

# Method selection dropdown
method = st.selectbox("Метод:", ["Базовый симплекс-метод", "В двойственную"], key="method")

# Action buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Очистить"):
        st.experimental_rerun()
with col2:
    solve = st.button("Решить")
with col3:
    dual = st.button("В двойственную")

# Handling the Solve button
if solve:
    st.write("**Результаты:**")
    # Placeholder for solving the linear programming problem
    st.write("Решение будет здесь.")
