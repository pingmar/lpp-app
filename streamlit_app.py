import streamlit as st

# Use HTML and CSS for custom styling
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
    }
    .container {
        width: 600px;
        margin: auto;
        padding: 20px;
        border: 2px solid #ccc;
        border-radius: 10px;
        background-color: #f9f9f9;
    }
    .title {
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
    }
    .section {
        margin-bottom: 20px;
    }
    .section label {
        display: block;
        margin-bottom: 5px;
    }
    .section input, .section select {
        width: 100%;
        padding: 5px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .checkbox-section {
        display: flex;
        gap: 10px;
    }
    .button-group {
        text-align: center;
        margin-top: 20px;
    }
    .button-group button {
        padding: 10px 20px;
        margin: 5px;
        border: none;
        border-radius: 5px;
        background-color: #007bff;
        color: white;
        cursor: pointer;
    }
    .button-group button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML structure for the page
st.markdown(
    """
    <div class="container">
        <div class="title">Linear Programming Solver</div>
        <div class="section">
            <label for="num_variables">Количество переменных:</label>
            <input type="number" id="num_variables" min="1" max="10" value="3">
        </div>
        <div class="section">
            <label for="num_constraints">Количество ограничений:</label>
            <input type="number" id="num_constraints" min="1" max="10" value="3">
        </div>
        <div class="section">
            <label>Целевая функция:</label>
            <div>
                <input type="number" placeholder="0"> x₁ +
                <input type="number" placeholder="0"> x₂ +
                <input type="number" placeholder="0"> x₃ →
                <select>
                    <option>min</option>
                    <option>max</option>
                </select>
            </div>
        </div>
        <div class="section">
            <label>Ограничения:</label>
            <div>
                <input type="number" placeholder="0"> x₁ +
                <input type="number" placeholder="0"> x₂ +
                <input type="number" placeholder="0"> x₃ 
                <select>
                    <option>≤</option>
                    <option>=</option>
                    <option>≥</option>
                </select>
                <input type="number" placeholder="0">
            </div>
            <div>
                <input type="number" placeholder="0"> x₁ +
                <input type="number" placeholder="0"> x₂ +
                <input type="number" placeholder="0"> x₃ 
                <select>
                    <option>≤</option>
                    <option>=</option>
                    <option>≥</option>
                </select>
                <input type="number" placeholder="0">
            </div>
            <div>
                <input type="number" placeholder="0"> x₁ +
                <input type="number" placeholder="0"> x₂ +
                <input type="number" placeholder="0"> x₃ 
                <select>
                    <option>≤</option>
                    <option>=</option>
                    <option>≥</option>
                </select>
                <input type="number" placeholder="0">
            </div>
        </div>
        <div class="section">
            x₁, x₂, x₃ ≥ 0
        </div>
        <div class="checkbox-section">
            <label><input type="checkbox"> В виде дробей</label>
            <label><input type="checkbox"> С решением</label>
        </div>
        <div class="section">
            <label for="method">Метод:</label>
            <select id="method">
                <option>Базовый симплекс-метод</option>
                <option>В двойственную</option>
            </select>
        </div>
        <div class="button-group">
            <button>Очистить</button>
            <button>Решить</button>
            <button>В двойственную</button>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
