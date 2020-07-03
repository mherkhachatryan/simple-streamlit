import time
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


pages = { "Main":2, "Exponential": 0, "Data": 1,}

st.markdown("""
## Welcome to Sample Streamlit app's Main page
To continue accept terms and conditions.

*We didn't add any terms, because no one reads it.
*
""")
terms_and_conditions = st.checkbox("Accept term and conditions")


# terms_and_conditions = st.checkbox("Accept term and conditions")

if terms_and_conditions:

    choice = st.sidebar.radio("Choice your page: ", tuple(pages.keys()))

    if choice == "Main":
        """
        # Welcome on the board 
        Choose one of the options in the sidebar to move forward 
        """


    elif choice == "Exponential":

        """
        # Simple Exponential Grapth
        """
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        poly_order = st.sidebar.slider("Choose Exponent Order", 0, 24, 2)
        domain_min = st.sidebar.number_input("Lower Bound", -10 ** 10, 10 ** 10, -100)
        domain_max = st.sidebar.number_input("Upper Bound", -10 ** 10, 10 ** 10, 100)
        domain = np.linspace(-1000, 1000, 100)
        polynomial = domain ** poly_order
        plt.plot(polynomial, color="orange")
        st.pyplot()

    elif choice == "Data":
        """
        ## Simple Example of Dataframes in Streamlit
        Iris dataset
        """

        data = load_iris()
        data = data.data
        st.dataframe(data)