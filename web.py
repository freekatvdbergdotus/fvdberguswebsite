import streamlit as st
import pandas

st.set_page_config(layout="wide")

df = pandas.read_csv("docs.csv", sep=";")

sections = [("adsl","aDSL publications"),
            ("idsl","iDSL publications"),
            ("thesis","Theses"),
            ("other","Other publications"),]

for section_id, section_name in sections:
    st.title(section_name)
    for index,row in df.iterrows():
        if section_id == row["category"]:
            st.write(f"[{row['name']}](app/static/{row["filename"]}.pdf)",
                     "<br>",row["authors"],
                     ",",row["source"],unsafe_allow_html=True)

