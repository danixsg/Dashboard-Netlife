import pandas as pd
import streamlit as st

# ===============================
# CARGA Y LIMPIEZA DE DATOS
# ===============================
@st.cache_data
def cargar_y_limpiar_datos():
    df_usuarios = pd.read_csv("datasets/acc_usuario.csv")
    df_logs = pd.read_csv("datasets/server_logs.csv")

    # Limpieza y preparación
    df_logs["fecha_hora_intento"] = pd.to_datetime(df_logs["fecha_hora_intento"])
    df_completo = pd.merge(df_logs, df_usuarios, on="usu_codigo", how="left")

    df_errores = df_completo[df_completo["estado_login"] == "Error"].copy()
    df_errores["kde_cedula_invalida"] = (
        df_errores["usu_cedula_ruc"]
        .astype(str)
        .str.contains("[a-zA-Z]", regex=True, na=False)
    )
    df_errores["cuenta_suspendida"] = df_errores["usu_estado"] == "Suspendido"

    def clasificar_causa(row):
        if pd.isna(row["usu_codigo"]) or str(row["usu_codigo"]).strip() == "":
            return "USUARIOS NO REGISTRADOS"
        elif row["cuenta_suspendida"]:
            return "CUENTA SUSPENDIDA"
        elif row["kde_cedula_invalida"]:
            return "CEDULA MAL FORMATEADA"
        else:
            return "FALLO DEL SERVIDOR"

    df_errores["causa_raiz"] = df_errores.apply(clasificar_causa, axis=1)

    # Extraer día de la semana y hora para responder tus preguntas más fácil
    df_errores["dia_semana"] = df_errores["fecha_hora_intento"].dt.day_name()
    df_errores["hora"] = df_errores["fecha_hora_intento"].dt.hour

    return df_usuarios, df_completo, df_errores


# Ejecutamos la función
df_usuarios, df_completo, df_errores = cargar_y_limpiar_datos()