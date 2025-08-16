import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import io

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

        # Crear figura 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Configuración de ejes
        ax.set_xlim([-1.2, 1.2])
        ax.set_ylim([-1.2, 1.2])
        ax.set_zlim([-1.2, 1.2])
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        # Eje z como campo B0
        ax.quiver(0, 0, 0, 0, 0, 1, color='r', linewidth=2, label="B₀")

        # Parámetros de la animación
        frames = 100
        t = np.linspace(0, 2*np.pi, frames)
        radius = 1.0

        x = radius * np.cos(omega * 1e6 * t / frames)
        y = radius * np.sin(omega * 1e6 * t / frames)
        z = np.zeros_like(t)

        point, = ax.plot([x[0]], [y[0]], [z[0]], 'bo', markersize=10)

        def update(i):
            point.set_data([x[i]], [y[i]])
            point.set_3d_properties(z[i])
            return point,

        ani = animation.FuncAnimation(fig, update, frames=frames, interval=100, blit=True)

        # Guardar en buffer como GIF
        buf = io.BytesIO()
        ani.save(buf, writer='pillow', format='gif')
        buf.seek(0)

        # Mostrar animación
        st.image(buf, caption="Precesión de protón alrededor de B₀", use_container_width=True)

    else:
        st.warning("Ingrese un valor de B₀ mayor que 0.")
