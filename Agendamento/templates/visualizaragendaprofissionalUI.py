import streamlit as st
from views import View
import time
from datetime import datetime
from datetime import timedelta

class VisualizarAgendaProfissionalUI:
    def main():
        st.header("Visualizar Agenda")
        View.horario_listar()

