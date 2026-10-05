import plotly.express as px
import streamlit as st

from src.data import load_titanic_data
from src.styles import apply_styles

st.set_page_config(
    page_title="Titanic | Bitácora",
    page_icon="◌",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_styles()

st.sidebar.markdown(
    """
    <div class="sidebar-brand">
        <span class="brand-mark">b.</span>
        <span>bitácora<span class="brand-dot">.</span></span>
    </div>
    <div class="sidebar-caption">LABORATORIO DE DATOS</div>
    """,
    unsafe_allow_html=True,
)

df = load_titanic_data()

st.markdown('<div class="eyebrow">PROYECTO 01 · ANÁLISIS EXPLORATORIO</div>', unsafe_allow_html=True)
st.title("A bordo del Titanic")
st.markdown(
    '<p class="page-intro">Una mirada a las personas que viajaron en el Titanic y a los factores '
    'que se relacionaron con su supervivencia.</p>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="context-note">
      <span class="note-mark">i</span>
      <span>Este conjunto de datos contiene información de <strong>891 pasajeros</strong> y es una
      muestra del manifiesto histórico. Las asociaciones observadas no implican causalidad.</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">EL CONJUNTO DE DATOS</div>', unsafe_allow_html=True)
metric1, metric2, metric3, metric4 = st.columns(4)
survival_rate = df["sobrevivio"].mean() * 100
metric1.metric("Pasajeros", f"{len(df):,}")
metric2.metric("Sobrevivieron", f"{survival_rate:.1f}%")
metric3.metric("Edad mediana", f"{df['edad'].median():.0f} años")
metric4.metric("Datos de edad ausentes", f"{df['edad'].isna().sum()}")

st.markdown('<div class="section-label section-label-spaced">EXPLORA LOS PERFILES</div>', unsafe_allow_html=True)
filter1, filter2, filter3 = st.columns([1, 1, 1.5])
with filter1:
    classes = st.multiselect(
        "Clase del pasaje",
        options=["Primera", "Segunda", "Tercera"],
        default=["Primera", "Segunda", "Tercera"],
    )
with filter2:
    genders = st.multiselect(
        "Género",
        options=["Mujer", "Hombre"],
        default=["Mujer", "Hombre"],
    )
with filter3:
    age_min = int(df["edad"].min())
    age_max = int(df["edad"].max())
    age_range = st.slider("Edad", min_value=age_min, max_value=age_max, value=(age_min, age_max))
    include_unknown_age = st.checkbox("Incluir edades no registradas", value=True)

age_matches = df["edad"].between(age_range[0], age_range[1])
if include_unknown_age:
    age_matches |= df["edad"].isna()
filtered = df[
    df["clase"].isin(classes)
    & df["genero"].isin(genders)
    & age_matches
]

if filtered.empty:
    st.info("No hay pasajeros que coincidan con estos filtros. Prueba con otra selección.")
else:
    chart1, chart2 = st.columns(2, gap="large")
    with chart1:
        survival = (
            filtered.groupby(["clase", "genero"], as_index=False)["sobrevivio"]
            .mean()
            .assign(sobrevivio=lambda data: data["sobrevivio"] * 100)
        )
        fig = px.bar(
            survival,
            x="clase",
            y="sobrevivio",
            color="genero",
            barmode="group",
            category_orders={"clase": ["Primera", "Segunda", "Tercera"]},
            color_discrete_map={"Mujer": "#bd7759", "Hombre": "#405d56"},
            labels={"clase": "Clase", "sobrevivio": "Supervivencia (%)", "genero": "Género"},
        )
        fig.update_layout(
            title="Supervivencia por clase y género",
            yaxis_range=[0, 100],
            yaxis_ticksuffix="%",
            legend_title_text="",
        )
        st.plotly_chart(fig, width="stretch")

    with chart2:
        ages = filtered.dropna(subset=["edad"]).copy()
        ages["resultado"] = ages["sobrevivio"].map({0: "No sobrevivió", 1: "Sobrevivió"})
        fig = px.histogram(
            ages,
            x="edad",
            color="resultado",
            nbins=24,
            barmode="overlay",
            opacity=0.78,
            color_discrete_map={"No sobrevivió": "#405d56", "Sobrevivió": "#bd7759"},
            labels={"edad": "Edad", "resultado": "Resultado"},
        )
        fig.update_layout(title="Distribución de edades", legend_title_text="")
        st.plotly_chart(fig, width="stretch")

st.markdown('<div class="section-label section-label-spaced">CALIDAD Y DETALLE</div>', unsafe_allow_html=True)
data_col, missing_col = st.columns([1.5, 1], gap="large")
with data_col:
    st.markdown("#### Una muestra de pasajeros")
    st.dataframe(
        filtered[["sobrevivio", "clase", "genero", "edad", "tarifa", "familiares"]]
        .rename(
            columns={
                "sobrevivio": "Sobrevivió",
                "clase": "Clase",
                "genero": "Género",
                "edad": "Edad",
                "tarifa": "Tarifa",
                "familiares": "Familiares a bordo",
            }
        )
        .head(12),
        hide_index=True,
        width="stretch",
    )
with missing_col:
    st.markdown("#### Valores ausentes")
    missing = df.isna().sum().rename("Ausentes").to_frame()
    missing = missing[missing["Ausentes"] > 0].sort_values("Ausentes", ascending=False)
    if missing.empty:
        st.success("No hay valores ausentes en las variables analizadas.")
    else:
        missing.index.name = "Variable"
        st.dataframe(missing, width="stretch")
    st.caption(
        f"Mostrando {len(filtered):,} de {len(df):,} pasajeros según los filtros seleccionados."
    )

st.markdown(
    '<div class="source-note">Fuente: conjunto Titanic de seaborn-data · '
    'Datos históricos de pasajeros utilizados con fines educativos.</div>',
    unsafe_allow_html=True,
)
