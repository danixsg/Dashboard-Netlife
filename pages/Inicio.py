from turtle import pd
import streamlit as st
from components.sidebar import mostrar_sidebar


mostrar_sidebar()


st.title("Inicio")



# ============================================================
# CSS ADAPTATIVO CLARO / OSCURO
# ============================================================

st.markdown(
    """
<style>


/* ============================= */
/* ESPACIADO GENERAL */
/* ============================= */


.block-container{

    padding-top:2rem;
    padding-left:3rem;
    padding-right:3rem;

}



/* ============================= */
/* TARJETAS GENERALES */
/* ============================= */


.net-card{

    background: var(--secondary-background-color);

    border-radius:22px;

    padding:30px;

    border:1px solid rgba(128,128,128,.25);

    box-shadow:
    0 8px 25px rgba(0,0,0,.08);

    transition:.25s;

}



.net-card:hover{

    transform:translateY(-5px);

    box-shadow:
    0 15px 35px rgba(0,0,0,.15);

}



/* ============================= */
/* HERO */
/* ============================= */


.hero{

    background:
    linear-gradient(
        135deg,
        rgba(0,174,239,.95),
        rgba(0,92,170,.95)
    );


    border-radius:28px;

    padding:45px;

    color:white;

    position:relative;

    overflow:hidden;


    box-shadow:
    0 15px 40px rgba(0,0,0,.18);


}



.hero:after{


    content:"";

    position:absolute;

    width:300px;

    height:300px;

    right:-100px;

    top:-100px;


    background:white;

    opacity:.12;

    border-radius:50%;


}



.hero h1{

    font-size:48px;

    font-weight:800;

    margin-bottom:10px;

}



.hero p{

    font-size:20px;

    opacity:.9;

}



/* ============================= */
/* BADGES */
/* ============================= */


.badge{

    display:inline-block;

    padding:8px 18px;

    margin-right:10px;

    margin-top:20px;


    background:rgba(255,255,255,.18);

    border-radius:50px;


    font-size:14px;

    font-weight:600;


    backdrop-filter:blur(10px);

}



/* ============================= */
/* TITULOS */
/* ============================= */


.section-title{


    font-size:30px;

    font-weight:750;

    margin-top:45px;

    margin-bottom:20px;


}

""",
    unsafe_allow_html=True,
)


# ============================================================
# HERO PRINCIPAL
# ============================================================


st.markdown(
    """
<div class="hero">


<h1>
📊 Netlife Access
</h1>


<p>
Dashboard Analítico de Registros de Autenticación
</p>


<span class="badge">
🔬 Ciencia de Datos
</span>


<span class="badge">
📅 Junio 2026
</span>


<span class="badge">
🚀 Análisis de Logs
</span>


</div>

""",
    unsafe_allow_html=True,
)

# ============================================================
# FLUJO DEL PROYECTO
# ============================================================


st.markdown(
    """
<div class="section-title">
🧭 Flujo del análisis
</div>
""",
    unsafe_allow_html=True,
)


st.markdown(
    """

<style>

.workflow-container{

display:flex;

align-items:center;

justify-content:space-between;

gap:15px;

margin-top:25px;

}


.workflow-item{

flex:1;

padding:25px 15px;

border-radius:20px;

text-align:center;

background:var(--secondary-background-color);

border:1px solid rgba(128,128,128,.25);

transition:.25s;

}



.workflow-item:hover{

transform:translateY(-8px);

border-color:#00AEEF;

}



.workflow-icon{

font-size:40px;

margin-bottom:12px;

}



.workflow-title{

font-size:18px;

font-weight:700;

}



.workflow-desc{

font-size:14px;

opacity:.75;

margin-top:8px;

}



.workflow-arrow{

font-size:30px;

color:#00AEEF;

font-weight:bold;

}



</style>



<div class="workflow-container">


<div class="workflow-item">

<div class="workflow-icon">
🎯
</div>

<div class="workflow-title">
1. Definición
</div>

<div class="workflow-desc">

Objetivo y preguntas<br>
de investigación

</div>

</div>



<div class="workflow-arrow">
➜
</div>



<div class="workflow-item">

<div class="workflow-icon">
📂
</div>

<div class="workflow-title">
2. Recopilación
</div>

<div class="workflow-desc">

Conjuntos de datos<br>
y obtención

</div>

</div>



<div class="workflow-arrow">
➜
</div>



<div class="workflow-item">

<div class="workflow-icon">
🧹
</div>

<div class="workflow-title">
3. Limpieza
</div>

<div class="workflow-desc">

Carga, exploración<br>
y preparación

</div>

</div>



<div class="workflow-arrow">
➜
</div>



<div class="workflow-item">

<div class="workflow-icon">
⚙️
</div>

<div class="workflow-title">
4. Procesamiento
</div>

<div class="workflow-desc">

Análisis e<br>
interpretación

</div>

</div>



<div class="workflow-arrow">
➜
</div>



<div class="workflow-item">

<div class="workflow-icon">
📄
</div>

<div class="workflow-title">
5. Documentación
</div>

<div class="workflow-desc">

Hallazgos, respuestas<br>
y recomendaciones

</div>

</div>



</div>

""",
    unsafe_allow_html=True,
)

# ============================================================
# FUENTES DE DATOS
# ============================================================


st.markdown(
    """
<div class="section-title">
📂 Fuentes de datos utilizadas
</div>
""",
    unsafe_allow_html=True,
)


col1, col2 = st.columns(2)


with col1:

    st.markdown(
        """

    <div class="net-card">

    <h2>📄 server_logs.csv</h2>

    <p>

    Registro histórico de intentos de autenticación
    realizados en la plataforma.

    </p>


    <br>

    <b>
    Contiene información sobre:
    </b>

    <br><br>

    🔹 Fecha y hora del intento

    <br>

    🔹 Plataforma de origen

    <br>

    🔹 Estado del inicio de sesión

    <br>

    🔹 Usuario asociado al intento


    </div>

    """,
        unsafe_allow_html=True,
    )


with col2:

    st.markdown(
        """

    <div class="net-card">

    <h2>👥 acc_usuario.csv</h2>


    <p>

    Catálogo de usuarios utilizado para
    complementar la información de los registros
    de conexión.

    </p>


    <br>

    <b>
    Contiene información sobre:
    </b>


    <br><br>


    🔹 Código del usuario

    <br>

    🔹 Identificador registrado

    <br>

    🔹 Estado de la cuenta

    <br>

    🔹 Token del dispositivo


    </div>

    """,
        unsafe_allow_html=True,
    )


# ============================================================
# OBJETIVO
# ============================================================


st.markdown(
    """
<div class="section-title">
🎯 Objetivo del análisis
</div>
""",
    unsafe_allow_html=True,
)


st.markdown(
    """

<div class="net-card">


<p>

En el último mes (junio), sabemos que los usuarios de nuestra aplicación Netlife Access
han experimentado errores ocasionales en la autenticación durante los procesos de inicio
de sesión y registro, lo que afecta nuestra meta de resolución al primer contacto.

</p>


<p>

No queremos tener que rastrear manualmente cada queja en el Call Center, pero podemos
acceder a los registros de conexión del servidor (Logs) y cruzarlos con nuestra base de
datos de usuarios (acc_usuario) para analizar el historial de accesos.

</p>


<p>

Sabemos que nuestros clientes intentan conectarse desde diferentes plataformas móviles y
web, y que algunas fallas pueden deberse al ingreso incorrecto de su identificador financiero
o a cuentas inhabilitadas.

</p>


<p>

Nuestro objetivo es reducir lo posible la lista de causas principales,
aislar los errores de formato de los usuarios, y determinar si existe un patrón técnico
focalizado con el fin de explicarle al equipo de Desarrollo TI dónde aplicar las
validaciones y los parches de seguridad.

</p>


</div>

""",
    unsafe_allow_html=True,
)


# ============================================================
# PREGUNTAS DE INVESTIGACIÓN
# ============================================================

st.markdown(
    """
<div class="section-title">
❓ Preguntas de investigación
</div>
""",
    unsafe_allow_html=True,
)


preguntas = [
    "¿En qué fechas se concentran las conexiones fallidas según los registros del servidor?",
    "¿En qué horas se concentran las conexiones fallidas según los registros del servidor?",
    "¿Qué día de la semana presenta mayor cantidad de errores?",
    "¿Qué plataforma de origen reporta la mayor cantidad de errores de conexión en el log?",
    "¿Qué porcentaje representa cada categoría de error al intentar autenticarse?",
    "¿Existe relación entre la plataforma utilizada y el tipo de error presentado?",
]


col1, col2 = st.columns(2)


for i, pregunta in enumerate(preguntas):

    with col1 if i % 2 == 0 else col2:

        with st.container(border=True):

            st.markdown(
                f"""
                <div style="
                    display:flex;
                    align-items:center;
                    gap:15px;
                ">
                
                <div style="
                    background:#00AEEF;
                    color:white;
                    width:38px;
                    height:38px;
                    border-radius:50%;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-weight:bold;
                    flex-shrink:0;
                ">
                {i+1}
                </div>

                <div>
                {pregunta}
                </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            # ============================================================
# EQUIPO DEL PROYECTO
# ============================================================

st.markdown(
    """
<div class="section-title">
👥 Equipo del proyecto
</div>
""",
    unsafe_allow_html=True,
)


col1, col2, col3 = st.columns(3)


integrantes = [
    ("👨‍💻", "JOEL ALEXANDER", "MUÑOZ VELEZ",""),
    ("👩‍💻", "GÉNESIS DANIELA", "SOLANO ORDOÑEZ",""),
    ("👨‍💻", "HUGO RAFAEL", "IGUASNIA JORDAN",""),
]


for col, integrante in zip([col1, col2, col3], integrantes):

    with col:

        with st.container(border=True):

            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    padding:10px;
                ">

                <div style="
                    font-size:55px;
                    margin-bottom:15px;
                ">
                {integrante[0]}
                </div>


                <div style="
                    font-size:18px;
                    font-weight:700;
                ">
                {integrante[1]}
                </div>


                <div style="
                    font-size:18px;
                    font-weight:700;
                ">
                {integrante[2]}
                </div>


                <br>


                <div style="
                    opacity:.75;
                    font-size:14px;
                ">
                {integrante[3]}
                </div>


                </div>
                """,
                unsafe_allow_html=True,
            )
