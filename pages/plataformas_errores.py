import streamlit as st
import pandas as pd
import plotly.express as px

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
        font-size: 2.6rem;
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

    /* Mejora de contorno para gráficos Plotly dentro de tarjetas (opcional) */
    .stPlotlyChart {
        background: transparent;
    }

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# CARGA DATOS
# ============================================================


@st.cache_data
def cargar_datos():

    logs = pd.read_csv("datasets/server_logs.csv")

    usuarios = pd.read_csv("datasets/acc_usuario.csv")

    return logs, usuarios


logs, usuarios = cargar_datos()


# ============================================================
# CLASIFICACIÓN DE ERRORES
# ============================================================


df = logs.merge(
    usuarios[["usu_codigo", "usu_cedula_ruc", "usu_estado"]],
    on="usu_codigo",
    how="left",
)


def clasificar_error(row):

    if row["estado_login"] == "Exitoso":

        return "Acceso exitoso"

    if pd.isna(row["usu_codigo"]) or row["usu_codigo"] == "":

        return "Usuario no registrado"

    if row["usu_estado"] == "Suspendido":

        return "Cuenta suspendida"

    cedula = str(row["usu_cedula_ruc"])

    if len(cedula) != 10 or not cedula.isdigit():

        return "Cédula mal formateada"

    return "Fallo servidor"


df["categoria_error"] = df.apply(clasificar_error, axis=1)


# Solo errores para este dashboard

errores = df[df["categoria_error"] != "Acceso exitoso"].copy()


# ============================================================
# HERO
# ============================================================


st.markdown(
    """
<div class="hero">

<h1>
📱 Plataformas y Errores
</h1>

<p>
Análisis de los fallos de autenticación según
la plataforma utilizada y la categoría del error.
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


plataformas = sorted(errores["plataforma_origen"].unique())


seleccion_plataformas = st.sidebar.multiselect(
    "📱 Plataforma", plataformas, default=plataformas
)


categorias = sorted(errores["categoria_error"].unique())


seleccion_categorias = st.sidebar.multiselect(
    "⚠ Categoría de error", categorias, default=categorias
)


df_filtrado = errores[
    errores["plataforma_origen"].isin(seleccion_plataformas)
    & errores["categoria_error"].isin(seleccion_categorias)
]


# ============================================================
# KPIS
# ============================================================


st.markdown(
    """
<div class="section">
📊 Indicadores del análisis
</div>
""",
    unsafe_allow_html=True,
)


total_errores = len(df_filtrado)


if total_errores > 0:

    plataforma_principal = df_filtrado["plataforma_origen"].value_counts().idxmax()

    error_principal = df_filtrado["categoria_error"].value_counts().idxmax()

else:

    plataforma_principal = "-"

    error_principal = "-"


c1, c2, c3 = st.columns(3)


kpis = [
    ("❌", "Errores analizados", total_errores),
    ("📱", "Plataforma dominante", plataforma_principal),
    ("⚠️", "Error principal", error_principal),
]


for col, kpi in zip([c1, c2, c3], kpis):

    with col:

        valor = kpi[2]

        if isinstance(valor, int):

            valor = f"{valor:,}"

        st.markdown(
            f"""
<div class="metric-card">


<h2>
{kpi[0]}
</h2>


<div class="metric-number">
{valor}
</div>


<div class="metric-label">
{kpi[1]}
</div>


</div>
""",
            unsafe_allow_html=True,
        )


# ============================================================
# ERRORES POR PLATAFORMA
# ============================================================


st.markdown(
    """
<div class="section">
📱 Errores por plataforma
</div>
""",
    unsafe_allow_html=True,
)


col1, col2 = st.columns(2)


with col1:

    plataforma_data = df_filtrado["plataforma_origen"].value_counts().reset_index()

    plataforma_data.columns = ["Plataforma", "Cantidad"]

    fig = px.bar(
        plataforma_data,
        x="Cantidad",
        y="Plataforma",
        orientation="h",
        text="Cantidad",
        title="Cantidad de errores por plataforma",
    )

    fig.update_layout(height=400)

    st.plotly_chart(fig, use_container_width=True)


with col2:

    error_data = df_filtrado["categoria_error"].value_counts().reset_index()

    error_data.columns = ["Error", "Cantidad"]

    fig = px.pie(
        error_data,
        names="Error",
        values="Cantidad",
        hole=0.55,
        title="Distribución de categorías",
    )

    st.plotly_chart(fig, use_container_width=True)


# ============================================================
# RELACIÓN PLATAFORMA ERROR
# ============================================================


st.markdown(
    """
<div class="section">
🔗 Relación entre plataforma y tipo de error
</div>
""",
    unsafe_allow_html=True,
)


heatmap = pd.crosstab(df_filtrado["plataforma_origen"], df_filtrado["categoria_error"])


fig = px.imshow(
    heatmap,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="Reds",
    title="Concentración de errores por plataforma",
)


st.plotly_chart(fig, use_container_width=True)


# ============================================================
# TABLA DETALLE
# ============================================================


st.markdown(
    """
<div class="section">
📋 Detalle del análisis
</div>
""",
    unsafe_allow_html=True,
)


tabla = (
    df_filtrado.groupby(["plataforma_origen", "categoria_error"])
    .size()
    .reset_index(name="Cantidad")
    .sort_values("Cantidad", ascending=False)
)


st.dataframe(tabla, use_container_width=True, hide_index=True)
