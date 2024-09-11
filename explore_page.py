import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data():
    # loading the diabeties dataset
    df = pd.read_csv('diabetes.csv')
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Diabetics patients Analysis")

    st.write(
        """
    ### Diabetics Patients Predictions
    """
    )

    data = df['Outcome'].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Number of Outcoms from the Daiabetic Dataset""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Mean Outcome Based On BMI
    """
    )

    # dt = df.groupby(["BMI"])["Outcome"].mean().sort_values(ascending=True)
    # data = pd.DataFrame(dt)
    plt.figure(figsize=(10,6))
    fig, ax =plt.subplots()
    sns.violinplot(x='Outcome', y='BMI', data = df, ax=ax)
    st.pyplot(plt)

    st.write(
        """
    #### Mean Outcome Based On Age
    """
    )

    data = df.groupby(["Age"])["Outcome"].mean().sort_values(ascending=True)
    st.line_chart(data)