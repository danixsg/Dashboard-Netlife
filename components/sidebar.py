import streamlit as st


def mostrar_sidebar():

    st.sidebar.markdown("""
    # 📊 Netlife Access

    ---
    """)

    st.sidebar.markdown(
        """
        <div class="sidebar-box">

        <b>📁 Navegación</b>

        <br><br>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.page_link("pages/Inicio.py", label="🏠 Inicio")

    st.sidebar.page_link("pages/resumen_general.py", label="📌 Resumen General")

    st.sidebar.page_link("pages/analisis_temporal.py", label="🕒 Análisis Temporal")

    st.sidebar.page_link(
        "pages/plataformas_errores.py", label="📱 Plataformas y Errores"
    )

