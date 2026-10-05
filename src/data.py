from pathlib import Path

import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "titanic.csv"


@st.cache_data
def load_titanic_data() -> pd.DataFrame:
    """Carga y prepara la muestra local de pasajeros del Titanic."""
    df = pd.read_csv(DATA_PATH)
    return df.rename(
        columns={
            "survived": "sobrevivio",
            "pclass": "clase_num",
            "sex": "genero_original",
            "age": "edad",
            "sibsp": "hermanos_conyuge",
            "parch": "padres_hijos",
            "fare": "tarifa",
            "embarked": "puerto",
            "class": "clase_original",
            "who": "grupo",
            "adult_male": "hombre_adulto",
            "deck": "cubierta",
            "embark_town": "ciudad_embarque",
            "alive": "resultado_original",
            "alone": "viaja_solo",
        }
    ).assign(
        clase=lambda data: data["clase_original"].map(
            {"First": "Primera", "Second": "Segunda", "Third": "Tercera"}
        ),
        genero=lambda data: data["genero_original"].map({"female": "Mujer", "male": "Hombre"}),
        familiares=lambda data: data["hermanos_conyuge"] + data["padres_hijos"],
    )
