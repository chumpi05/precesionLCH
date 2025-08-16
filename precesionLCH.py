import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constante giromagnética del protón (MHz/T)
GAMMA = 42.577478518  # MHz/T

st.title("⚛️ Precesión de Protones - Ley de Larmor")
st.write("Visualización interactiva del movimiento de precesión de los protones de Hidrógeno en un campo magnético principal B₀.")

# Entrada de valor para B0
B0 = st.number_input("Ingrese el valor del campo magnético B₀ (Tesla):", min_value=0.0, step=0.1, format="%.3f")

if st.button("Calcular y mostrar precesión"):
    if B0 > 0:
        # Frecuencia de Larmor en MHz
        omega = GAMMA * B0  # MHz
        st.write(f"**Frecuencia de precesión ω = {omega:.3f} MHz**")

        # Crear animación de precesión
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Eje z es el campo B0
        ax.quiver(0, 0, 0, 0, 0, 1, color='r', linewidth=2, label="B₀")

        # Parámetros de la animación
        frames = 200
        t = np.linspace(0, 2*np.pi, frames)
        radius = 1.0

        # Posición inicial
        x = radius * np.cos(2 * np.pi * omega * 1e6 * t / frames)
        y = radius * np.sin(2 * np.pi * omega * 1e6 * t / frames)
        z = np.zeros_like(t)

        point, = ax.plot([x[0]], [y[0]], [z[0]], 'bo', markersize=10)
        circle, = ax.plot(x, y, z, 'b--', alpha=0.3)

        def update(i):
            point.set_data([x[i]], [y[i]])
            point.set_3d_properties(z[i])
            return point,

        ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

        st.pyplot(fig)
    else:
        st.warning("Ingrese un valor de B₀ mayor que 0.")
