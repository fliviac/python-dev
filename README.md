# Bitácora — exploración de datos

Aplicación multipágina hecha con Streamlit: una portada editorial y un proyecto
interactivo de análisis exploratorio del conjunto de pasajeros del Titanic.

## Estructura

```text
.
├── .streamlit/
│   └── config.toml
├── data/
│   └── titanic.csv
├── pages/
│   └── 1_Analisis_Titanic.py
├── src/
│   ├── __init__.py
│   ├── data.py
│   └── styles.py
├── app.py
└── requirements.txt
```

## Ejecutar localmente

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

La aplicación ofrece filtros por clase, género y edad; métricas resumidas,
gráficos interactivos y un vistazo a los datos ausentes. El conjunto local
contiene 891 filas y procede del dataset `titanic` publicado en
[seaborn-data](https://github.com/mwaskom/seaborn-data).
