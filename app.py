import streamlit as st
import pandas as pd
import plotly.express as px

# Настройки страницы
st.set_page_config(page_title="Z-фактор Визуализация", layout="wide")

# Заголовок
st.title("📊 Визуализация фазового поведения Z = f(Pressure, Temperature)")
st.markdown("Данные загружены из Excel-файла `Z_values_table.xlsx`")

# Загрузка данных
try:
    df = pd.read_excel("Z_values_table.xlsx")
    st.success("✅ Файл успешно загружен!")
except Exception as e:
    st.error(f"❌ Ошибка загрузки Excel: {e}")
    st.stop()

# Отображение таблицы
st.subheader("📋 Таблица исходных данных")
st.dataframe(df)

# Проверка нужных колонок
if all(col in df.columns for col in ['Pressure', 'Temperature', 'Z']):
    # 3D-график
    st.subheader("📈 3D-график: Z = f(Pressure, Temperature)")
    fig3d = px.scatter_3d(df, x='Pressure', y='Temperature', z='Z',
                          color='Z',
                          title="3D Z-фактор",
                          labels={'Pressure': 'Pressure', 'Temperature': 'Temperature', 'Z': 'Z-factor'})
    st.plotly_chart(fig3d, use_container_width=True)

    # Тепловая карта (2D)
    st.subheader("🌡️ Тепловая карта: Z = f(Pressure, Temperature)")
    fig2d = px.density_heatmap(df, x='Pressure', y='Temperature', z='Z',
                               title="Heatmap: Z-фактор",
                               nbinsx=20, nbinsy=20,
                               color_continuous_scale="Viridis")
    st.plotly_chart(fig2d, use_container_width=True)

else:
    st.error("❗ В Excel-файле должны быть колонки: Pressure, Temperature, Z")
