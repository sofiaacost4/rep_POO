import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Cálculos com retângulo :o")
        base = st.text_input("Informe o valor da base do retângulo: ")
        altura = st.text_input("Informe o valor da altura do retângulo: ")
        if st.button("Calcular"):
            b = float(base)
            h = float(altura)
            r = Retangulo(b, h)
            st.write(r)
            st.write(r.calc_area())
            st.write(r.calc_diagonal())
            
            