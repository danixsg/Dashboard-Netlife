import streamlit as st


st.set_page_config(
    page_title="Netlife Access",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


inicio = st.Page(
    "pages/Inicio.py",
    title="Inicio",
    icon="🏠"
)


resumen = st.Page(
    "pages/resumen_general.py",
    title="Resumen General",
    icon="📌"
)


analisis = st.Page(
    "pages/analisis_temporal.py",
    title="Análisis Temporal",
    icon="🕒"
)


plataformas = st.Page(
    "pages/plataformas_errores.py",
    title="Plataformas y Errores",
    icon="📱"
)


pg = st.navigation(
    [
        inicio,
        resumen,
        analisis,
        plataformas
    ],
    position="hidden"
)


pg.run()