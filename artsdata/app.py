import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly-express


st.set_page_config(page_title='Excel Plotter')
st.title('Arts Data Plot📈')
st.subheader('Feed me with Excel file')

uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)
    groupby_column = st.selectbox(
        'What would you like to analyse?',
        ('program','members')
    )

    # -- GROUP DATAFRAME
    output_columns = ['lead_name']
    df_grouped = df.groupby(by=[groupby_column], as_index=False)['lead_name'].agg(lambda x: ', '.join(x))

    # -- PLOT DATAFRAME
    fig = px.bar(
        df_grouped,
        x=groupby_column,
        y='lead_name',
        
        
        template='plotly_white',
        
    )
    st.plotly_chart(fig)

   