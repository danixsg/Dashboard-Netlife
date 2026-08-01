import streamlit as st
import pandas as pd
import plotly.express as px
from components.sidebar import mostrar_sidebar

# 1. IMPORTAR LOS DATOS LIMPIOS DESDE datos.py
from datos import cargar_y_limpiar_datos

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

    /* Hero */
    .hero {
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
    .hero::after {
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
    .hero h1 {
        font-size: 2.6rem;
        font-weight: 700;
        margin: 0 0 0.25rem 0;
        letter-spacing: -0.02em;
    }
    .hero p {
        font-size: 1.1rem;
        margin-top: 0.6rem;
        opacity: 0.9;
        line-height: 1.6;
        max-width: 80%;
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

    /* Tarjetas generales */
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
    .metric-card h2 {
        font-size: 2.6rem;
        margin: 0 0 0.2rem 0;
        font-weight: 400;
    }
    .metric-number {
        font-size: 2.2rem;
        font-weight: 800;
        color: var(--text-color);
        margin: 0.4rem 0 0.2rem 0;
        line-height: 1.2;
    }
    .metric-label {
        color: var(--text-color-secondary);
        font-weight: 500;
        font-size: 0.95rem;
        letter-spacing: 0.02em;
        opacity: 1;
    }

    /* Ajuste de espaciado en columnas */
    .row-widget.stColumns {
        gap: 0.8rem;
    }

    /* Fondo transparente para respetar tema de Streamlit */
    .stApp, .main .block-container {
        background: transparent;
    }

    .stPlotlyChart {
        background: transparent;
    }
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# CARGA Y PREPARACIÓN DE DATOS
# ============================================================
df_usuarios, df_completo, df_errores = cargar_y_limpiar_datos()

# Preparar columnas de fecha, hora y día
df_errores['fecha'] = df_errores['fecha_hora_intento'].dt.date
df_errores['hora'] = df_errores['fecha_hora_intento'].dt.hour
df_errores['dia_semana'] = df_errores['fecha_hora_intento'].dt.day_name()

mapeo_dias = {
    'Monday': 'Lunes', 'Tuesday': 'Martes', 'Wednesday': 'Miércoles',
    'Thursday': 'Jueves', 'Friday': 'Viernes', 'Saturday': 'Sábado', 'Sunday': 'Domingo'
}
df_errores['dia_semana_esp'] = df_errores['dia_semana'].map(mapeo_dias)


# ============================================================
# HERO
# ============================================================
st.markdown(
    """
<div class="hero">
<h1>🕒 Análisis Temporal</h1>
<p>
Objetivo: Detectar cuándo ocurren los problemas de autenticación y aislar eventos anómalos en el tiempo.
</p>
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# FILTROS
# ============================================================
st.sidebar.markdown("---")
st.sidebar.subheader("⚙️ Filtros")

# Obtener fechas mínima y máxima del dataset
fecha_minima = df_errores['fecha'].min()
fecha_maxima = df_errores['fecha'].max()

# Crear el selector de rango de fechas
rango_fechas = st.sidebar.date_input(
    "📅 Rango de fechas",
    value=(fecha_minima, fecha_maxima),
    min_value=fecha_minima,
    max_value=fecha_maxima
)

# Validar que el usuario haya seleccionado inicio y fin
if len(rango_fechas) == 2:
    fecha_inicio, fecha_fin = rango_fechas
else:
    fecha_inicio = rango_fechas[0]
    fecha_fin = rango_fechas[0]

# Filtrar el DataFrame basado en la selección
df_filtrado = df_errores[(df_errores['fecha'] >= fecha_inicio) & (df_errores['fecha'] <= fecha_fin)]


# ============================================================
# KPIS / INDICADORES GENERALES
# ============================================================
st.markdown(
    """
<div class="section">
📊 Indicadores Generales
</div>
""",
    unsafe_allow_html=True,
)

# Cálculos para responder a las preguntas con el DataFrame filtrado
if len(df_filtrado) > 0:
    fecha_critica = str(df_filtrado['fecha'].value_counts().idxmax())
    hora_pico = f"{df_filtrado['hora'].value_counts().idxmax()}:00 hrs"
    dia_peor = str(df_filtrado['dia_semana_esp'].value_counts().idxmax())
else:
    fecha_critica = "-"
    hora_pico = "-"
    dia_peor = "-"

c1, c2, c3 = st.columns(3)

kpis = [
    ("📅", "Fecha con más fallos", fecha_critica),
    ("⏰", "Hora crítica", hora_pico),
    ("📆", "Día con más errores", dia_peor),
]

for col, kpi in zip([c1, c2, c3], kpis):
    with col:
        st.markdown(
            f"""
<div class="metric-card">
<h2>{kpi[0]}</h2>
<div class="metric-number">{kpi[2]}</div>
<div class="metric-label">{kpi[1]}</div>
</div>
""",
            unsafe_allow_html=True,
        )


# ============================================================
# GRÁFICO 1: ERRORES POR FECHA
# ============================================================
st.markdown('<div class="section">🗓️ Conexiones Fallidas por Fecha</div>', unsafe_allow_html=True)

if len(df_filtrado) > 0:
    errores_fecha = df_filtrado.groupby(['fecha', 'causa_raiz']).size().reset_index(name='Cantidad')
    totales_fecha = df_filtrado.groupby('fecha').size().reset_index(name='Cantidad')
    totales_fecha['causa_raiz'] = 'Total de Errores'
    df_plot1 = pd.concat([errores_fecha, totales_fecha])

    fig1 = px.line(
        df_plot1, x='fecha', y='Cantidad', color='causa_raiz', markers=True,
        labels={'fecha': 'Fecha', 'Cantidad': 'Número de Conexiones Fallidas', 'causa_raiz': 'Causa Raíz'},
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig1.update_layout(hovermode="x unified", height=450)
    st.plotly_chart(fig1, use_container_width=True)
else:
    st.info("No hay datos para las fechas seleccionadas.")

st.markdown("💡 Se observa una tendencia estable durante el mes, interrumpida por un pico crítico y anómalo el 26 de junio. Este aumento masivo está impulsado por 'Usuarios No Registrados' y 'Fallos del Servidor', lo que sugiere un ataque (DoS) o peticiones automatizadas.")


# ============================================================
# GRÁFICO 2: ERRORES POR HORA
# ============================================================
st.markdown('<div class="section">⌛ Conexiones Fallidas por Hora del Día</div>', unsafe_allow_html=True)

if len(df_filtrado) > 0:
    errores_hora = df_filtrado.groupby(['hora', 'causa_raiz']).size().reset_index(name='Cantidad')
    totales_hora = df_filtrado.groupby('hora').size().reset_index(name='Cantidad')
    totales_hora['causa_raiz'] = 'Total de Errores'
    df_plot2 = pd.concat([errores_hora, totales_hora])

    fig2 = px.line(
        df_plot2, x='hora', y='Cantidad', color='causa_raiz', markers=True,
        labels={'hora': 'Hora del Día (0-23)', 'Cantidad': 'Número de Conexiones Fallidas', 'causa_raiz': 'Causa Raíz'},
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    fig2.update_layout(hovermode="x unified", xaxis=dict(tickmode='linear', tick0=0, dtick=1), height=450)
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("No hay datos para las fechas seleccionadas.")

st.markdown("💡 Al evaluar las horas, el sistema no reporta congestión en horarios regulares. La enorme mayoría de los errores se agrupan en un pico extremo exactamente a las 10:00 a.m., confirmando la franja horaria del incidente técnico masivo.")


# ============================================================
# GRÁFICO 3: ERRORES POR DÍA DE LA SEMANA
# ============================================================
st.markdown('<div class="section">🚨 Conexiones Fallidas por Día de la Semana</div>', unsafe_allow_html=True)

if len(df_filtrado) > 0:
    errores_dia = df_filtrado['dia_semana_esp'].value_counts().reset_index()
    errores_dia.columns = ['Día', 'Cantidad']
    orden_dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    errores_dia['Día'] = pd.Categorical(errores_dia['Día'], categories=orden_dias, ordered=True)
    errores_dia = errores_dia.sort_values('Día')

    total = errores_dia['Cantidad'].sum()
    errores_dia['Porcentaje'] = (errores_dia['Cantidad'] / total * 100).round(1).astype(str) + '%'

    fig3 = px.bar(
        errores_dia, x='Cantidad', y='Día', orientation='h', text='Porcentaje',
        labels={'Cantidad': 'Número de Errores', 'Día': 'Día de la Semana'},
        color='Cantidad', color_continuous_scale='Viridis'
    )
    fig3.update_traces(textposition='outside')
    fig3.update_layout(coloraxis_showscale=False, height=450) 
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("No hay datos para las fechas seleccionadas.")

st.markdown("💡 El día viernes acumula el mayor volumen de errores del mes, pero este dato está fuertemente sesgado por el evento masivo del viernes 26 de junio. El resto de los días mantiene una distribución equitativa de fallos.")