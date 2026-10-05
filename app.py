import streamlit as st

from src.styles import apply_styles

st.set_page_config(
    page_title="Bitácora | Datos y exploración",
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

st.markdown('<div class="eyebrow">DATOS · HISTORIAS · DESCUBRIMIENTOS</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="hero">
      <div class="hero-copy">
        <div class="hero-kicker"><span class="status-dot"></span> Un espacio para explorar</div>
        <h1>Los datos también<br>cuentan <em>historias.</em></h1>
        <p>Una bitácora visual para entender lo que hay detrás de cada conjunto de datos.
        Empieza explorando uno de los viajes más conocidos de la historia.</p>
      </div>
      <div class="hero-art" aria-hidden="true">
        <div class="art-orbit orbit-one"></div>
        <div class="art-orbit orbit-two"></div>
        <div class="art-sun"></div>
        <div class="art-ship">TITANIC<br><span>1912</span></div>
        <div class="art-label label-top">41° 43′ N</div>
        <div class="art-label label-bottom">ATLÁNTICO NORTE</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1, 1], gap="large")
with left:
    st.markdown(
        """
        <div class="section-label">01 — PROYECTO DESTACADO</div>
        <h2 class="home-title">El viaje del Titanic</h2>
        <p class="body-copy">¿Quién tuvo más posibilidades de sobrevivir? Explora los datos
        de los pasajeros, compara grupos y encuentra patrones en una tragedia que marcó la historia.</p>
        """,
        unsafe_allow_html=True,
    )
    st.page_link(
        "pages/1_Analisis_Titanic.py",
        label="Explorar el análisis",
        icon="↗",
        width="content",
    )

with right:
    st.markdown(
        """
        <div class="mini-card">
          <div class="mini-card-top"><span class="mini-icon">✳</span><span>EN ESTE PROYECTO</span></div>
          <div class="mini-items">
            <div><span class="mini-number">01</span><span>Conoce el conjunto de datos</span></div>
            <div><span class="mini-number">02</span><span>Compara supervivencia por grupo</span></div>
            <div><span class="mini-number">03</span><span>Explora edades y calidad de los datos</span></div>
          </div>
          <div class="mini-card-foot">Un recorrido interactivo · 5 minutos</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="home-divider"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="home-footer">
      <span>HECHO PARA CURIOSOS</span>
      <span>Una demo de análisis exploratorio con Streamlit</span>
    </div>
    """,
    unsafe_allow_html=True,
)
