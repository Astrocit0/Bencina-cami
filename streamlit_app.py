import streamlit as st

def viajes(precio_bencina, numero_pasajeros, n_idas, n_vueltas):
    precio_total = 40 / 17 * precio_bencina * (n_idas + n_vueltas) * (1 / numero_pasajeros)
    return precio_total

st.title("Calculadora de Costos de Viaje por persona a Vilcun en Auto Cami _Doña Rabias_")

precio_bencina = st.number_input("Precio de la bencina (por litro)", min_value=0.0)
numero_pasajeros = st.number_input("Número de pasajeros", min_value=1, step=1)
n_idas = st.number_input("Número de idas", min_value=0, step=1)
n_vueltas = st.number_input("Número de vueltas", min_value=0, step=1)

if st.button("Calcular"):
    costo_total = viajes(precio_bencina, numero_pasajeros, n_idas, n_vueltas)
    st.write(f"El costo total del viaje por persona es: {costo_total}")
