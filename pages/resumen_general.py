import streamlit as st
import pandas as pd

from components.sidebar import mostrar_sidebar


# ============================================================
# SIDEBAR
# ============================================================

mostrar_sidebar()


# ============================================================
# ESTILOS MEJORADOS (RESPETANDO TEMA CLARO/OSCURO)
# ============================================================

st.markdown(
"""
<style>
    /* Variables de diseño usando los colores nativos de Streamlit */
    :root {
        --primary-dark: #0a2e4a;
        --primary-mid: #1a5f7a;
        --primary-light: #3b8ea5;
        --accent: #00b4d8;
        --radius-lg: 28px;
        --radius-md: 20px;
        --radius-sm: 14px;
        --transition: all 0.25s ease;
    }

    /* Hero - usamos gradiente fijo pero con colores que funcionan en ambos modos,
       el texto blanco es legible sobre el gradiente oscuro. */
    .hero-container {
        background: linear-gradient(135deg, #0a2e4a 0%, #1a5f7a 60%, #3b8ea5 100%);
        padding: 2.8rem 3.2rem;
        border-radius: var(--radius-lg);
        color: white;
        margin-bottom: 2.8rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
        border: 1px solid rgba(255,255,255,0.08);
        position: relative;
        overflow: hidden;
    }
    .hero-container::after {
        content: '';
        position: absolute;
        top: -30%;
        right: -10%;
        width: 300px;
        height: 300px;
        background: rgba(255,255,255,0.04);
        border-radius: 50%;
        pointer-events: none;
    }
    .hero-container h1 {
        font-size: 2.6rem;
        font-weight: 700;
        margin: 0 0 0.25rem 0;
        letter-spacing: -0.02em;
    }
    .hero-container p {
        font-size: 1.1rem;
        margin-top: 0.6rem;
        opacity: 0.9;
        line-height: 1.6;
        max-width: 80%;
    }
    .hero-container b {
        color: #b3e4f5;
        font-weight: 600;
    }

    /* Títulos de sección */
    .section {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 2.8rem;
        margin-bottom: 1.5rem;
        color: var(--text-color);
        padding-bottom: 0.4rem;
        border-bottom: 3px solid var(--primary-light);
        display: inline-block;
        letter-spacing: -0.01em;
    }

    /* Tarjetas generales usando variables de Streamlit */
    .card {
        background: var(--secondary-background-color);
        border-radius: var(--radius-md);
        padding: 1.8rem 2rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        border: 1px solid var(--border-color);
        transition: var(--transition);
        height: 100%;
    }
    .card:hover {
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }
    .card h2, .card h3 {
        color: var(--text-color);
        font-weight: 600;
        margin-top: 0;
        margin-bottom: 1rem;
    }
    .card h2 {
        font-size: 1.5rem;
    }
    .card h3 {
        font-size: 1.25rem;
    }

    /* Tarjetas de métricas (KPIs) */
    .metric-card {
        background: var(--secondary-background-color);
        border-radius: var(--radius-md);
        padding: 1.8rem 1rem;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        border: 1px solid var(--border-color);
        transition: var(--transition);
        height: 100%;
    }
    .metric-card:hover {
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
        transform: translateY(-3px);
    }
    .metric-icon {
        font-size: 2.6rem;
        margin-bottom: 0.2rem;
        display: block;
    }
    .metric-number {
        font-size: 2.6rem;
        font-weight: 800;
        color: var(--text-color);
        margin: 0.4rem 0 0.2rem 0;
        line-height: 1.2;
    }
    .metric-title {
        color: var(--text-color-secondary);
        font-weight: 500;
        font-size: 0.95rem;
        letter-spacing: 0.02em;
    }

    /* Barra de progreso */
    .status-bar {
        width: 100%;
        height: 12px;
        background: var(--border-color);
        border-radius: 30px;
        overflow: hidden;
        margin: 0.75rem 0 1.4rem 0;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }
    .status-progress {
        height: 100%;
        background: linear-gradient(90deg, #1a5f7a, #3b8ea5, #00b4d8);
        border-radius: 30px;
        transition: width 0.8s cubic-bezier(0.22, 1, 0.36, 1);
        width: 0%; /* se setea inline */
    }

    /* Líneas de información dentro de tarjetas */
    .info-line {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.75rem 0;
        border-bottom: 1px solid var(--border-color);
        font-size: 1rem;
        color: var(--text-color);
    }
    .info-line:last-child {
        border-bottom: none;
    }
    .info-line b {
        color: var(--text-color);
        font-weight: 600;
    }

    /* Tags (etiquetas) */
    .tag {
        display: inline-block;
        background: var(--border-color);
        color: var(--text-color);
        padding: 0.25rem 1.2rem;
        border-radius: 40px;
        font-size: 0.9rem;
        font-weight: 500;
        margin: 0.2rem 0.3rem 0.2rem 0;
        border: 1px solid rgba(0,0,0,0.05);
    }

    /* Ajuste para el pie de página (cierre) */
    .card center {
        color: var(--text-color-secondary);
        font-size: 0.95rem;
        line-height: 1.6;
    }
    .card center strong {
        color: var(--text-color);
    }

    /* Ajuste de espaciado en el contenedor de KPIs */
    .row-widget.stColumns {
        gap: 0.8rem;
    }

    /* Eliminamos cualquier fondo fijo para respetar el tema de Streamlit */
    .stApp, .main .block-container {
        background: transparent;
    }

    /* Mejoramos la legibilidad del número dentro de la tarjeta de estado */
    .card .metric-number {
        font-size: 2.8rem;
        margin: 0.2rem 0 0.6rem 0;
    }

</style>
""",
unsafe_allow_html=True
)


# ============================================================
# DATOS
# ============================================================

@st.cache_data
def cargar_datos():

    logs = pd.read_csv(
        "datasets/server_logs.csv",
        parse_dates=[
            "fecha_hora_intento"
        ]
    )


    usuarios = pd.read_csv(
        "datasets/acc_usuario.csv"
    )


    return logs, usuarios



logs, usuarios = cargar_datos()



# ============================================================
# CALCULOS
# ============================================================

total_registros = int(len(logs))


total_usuarios = int(len(usuarios))


exitosos = int(
    (logs["estado_login"] == "Exitoso").sum()
)


fallidos = int(
    (logs["estado_login"] == "Error").sum()
)



porcentaje_exito = round(
    (exitosos / total_registros) * 100,
    1
)



activos = int(
    (usuarios["usu_estado"] == "Activo").sum()
)


suspendidos = int(
    (usuarios["usu_estado"] == "Suspendido").sum()
)



fecha_inicio = (
    logs["fecha_hora_intento"]
    .min()
    .strftime("%d/%m/%Y")
)


fecha_fin = (
    logs["fecha_hora_intento"]
    .max()
    .strftime("%d/%m/%Y")
)



# ============================================================
# HERO
# ============================================================

st.markdown(
f"""
<div class="hero-container">

<h1>
📌 Netlife Access
</h1>

<p>
Resumen ejecutivo del sistema de autenticación.
<br><br>

Periodo evaluado:
<b>{fecha_inicio}</b>
hasta
<b>{fecha_fin}</b>

</p>

</div>
""",
unsafe_allow_html=True
)



# ============================================================
# KPIS
# ============================================================

st.markdown(
"""
<div class="section">
📊 Indicadores generales
</div>
""",
unsafe_allow_html=True
)



kpis = [

    ("📄","Registros analizados",total_registros),

    ("👥","Usuarios registrados",total_usuarios),

    ("✅","Accesos exitosos",exitosos),

    ("❌","Errores registrados",fallidos)

]



cols = st.columns(4)



for col, kpi in zip(cols,kpis):

    with col:

        st.markdown(
f"""
<div class="metric-card">

<div class="metric-icon">
{kpi[0]}
</div>


<div class="metric-number">
{kpi[2]:,}
</div>


<div class="metric-title">
{kpi[1]}
</div>


</div>
""",
unsafe_allow_html=True
        )



# ============================================================
# ESTADO DEL SERVICIO
# ============================================================


st.markdown(
"""
<div class="section">
🟢 Estado general del servicio
</div>
""",
unsafe_allow_html=True
)



st.markdown(
f"""
<div class="card">

<h2>
Nivel de autenticaciones exitosas
</h2>


<div class="metric-number">
{porcentaje_exito}%
</div>


<div class="status-bar">

<div class="status-progress"
style="width:{porcentaje_exito}%">

</div>

</div>


<br>


<div class="info-line">

✅ Accesos correctos:
<b>{exitosos:,}</b>

</div>


<div class="info-line">

❌ Intentos fallidos:
<b>{fallidos:,}</b>

</div>


</div>
""",
unsafe_allow_html=True
)



# ============================================================
# INFORMACION DEL DATASET
# ============================================================


st.markdown(
"""
<div class="section">
📂 Información del análisis
</div>
""",
unsafe_allow_html=True
)



col1,col2 = st.columns(2)



with col1:

    st.markdown(
f"""
<div class="card">

<h3>
📄 Fuentes utilizadas
</h3>


<div class="tag">
server_logs.csv
</div>


<div class="tag">
acc_usuario.csv
</div>


<br><br>


Cantidad de registros procesados:

<h2>
{total_registros:,}
</h2>


</div>
""",
unsafe_allow_html=True
    )



with col2:

    st.markdown(
f"""
<div class="card">

<h3>
👤 Estado del catálogo
</h3>


<div class="info-line">

🟢 Usuarios activos:
<b>{activos:,}</b>

</div>


<div class="info-line">

🔴 Usuarios suspendidos:
<b>{suspendidos:,}</b>

</div>


<div class="info-line">

👥 Total usuarios:
<b>{total_usuarios:,}</b>

</div>


</div>
""",
unsafe_allow_html=True
    )



# ============================================================
# CIERRE
# ============================================================


st.markdown(
"""
<br>

<div class="card">

<center>

📌 Esta sección presenta una visión general del conjunto
de datos. Los análisis detallados de comportamiento,
patrones temporales y relación entre variables se
encuentran desarrollados en los dashboards posteriores.

</center>

</div>

""",
unsafe_allow_html=True
)